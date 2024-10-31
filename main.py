from flask import Flask, render_template, request
import boto3
from datetime import datetime
import uuid
from decimal import Decimal
import pandas as pd
from report import Report
import os

app = Flask(__name__)


# Access the AWS credentials and region from environment variables
aws_access_key_id = os.getenv('aws_access_key_id')
aws_secret_access_key = os.getenv('aws_secret_access_key')
aws_region = os.getenv('aws_default_region')

# Initialize the DynamoDB resource with the region from environment variable
dynamodb = boto3.resource(
    'dynamodb',
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Initialize the DynamoDB client
user_expenses_table = dynamodb.Table('user_expenses')

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    success_message = ""
    if request.method == 'POST':
        # Logic to handle form submission
        description = request.form['description']
        amount = Decimal(request.form['amount'])
        category = request.form['category']

        current_date = datetime.now().strftime('%Y-%m-%d')

        # Prepare the item to insert into the DynamoDB table
        item = {
            'id': str(uuid.uuid4()),
            'date': current_date,
            'category': category,
            'description': description,
            'amount': amount,
        }

        user_expenses_table.put_item(Item=item)

        success_message = "Expense added successfully!"

        # Render the form with the success message if it exists

    return render_template('expenses_insertion.html', success_message=success_message)


@app.route('/report')
def view_report():
    table_scan = user_expenses_table.scan()
    user_expenses = pd.DataFrame(table_scan['Items'])

    if user_expenses.empty:
        message = "No expenses found. Please add some expenses to generate a report."
        return render_template('report.html', chart_filename=None, message=message)

    user_expenses_report = Report(user_expenses)
    chart_filename = user_expenses_report.generate_spending_pie_chart()
    return render_template('report.html', chart_filename=chart_filename)  # Pass the filename to the template


@app.route('/dashboard')
def dashboard():
    chart_filename = request.args.get('chart_filename')  # Get the filename dynamically from the URL
    return render_template(chart_filename)  # Render the chart HTML dynamically


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
