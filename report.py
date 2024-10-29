import plotly.graph_objects as go
import plotly.express as px  # For accessing the color palette
import uuid

class Report:
    def __init__(self, transactions_df):
        self.transactions_df = transactions_df

    def generate_spending_pie_chart(self):
        # Generate a unique filename
        unique_filename = f"spending_pie_chart_{uuid.uuid4().hex}.html"

        # Standardize category names
        self.transactions_df['category'] = self.transactions_df['category'].str.strip().str.lower()

        # Aggregate amounts by category
        aggregated_data = self.transactions_df.groupby('category', as_index=False)['amount'].sum()

        # Create a Pie chart
        fig = go.Figure(
            data=[go.Pie(labels=aggregated_data['category'],
                         values=aggregated_data['amount'],
                         hoverinfo='label+percent',
                         texttemplate='%{value}$',  # Adding the dollar sign before the value
                         textinfo='text',  # Shows both the label and the formatted text
                         textfont_size=14,
                         marker=dict(colors=px.colors.qualitative.Plotly))]  # Set colors from Plotly's palette
        )

        # Update layout to match the design of the app
        fig.update_layout(
            title="Spending by Category",
            title_font=dict(size=24, color='#333', family='Arial, sans-serif'),
            margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins to center the pie chart
            paper_bgcolor='#f4f4f4',  # Background color to match the page style
            plot_bgcolor='#fff',
            height=585,
            width=985,
        )

        # Save the figure as an HTML file
        chart_path = f"templates/{unique_filename}"
        fig.write_html(chart_path)

        return unique_filename
