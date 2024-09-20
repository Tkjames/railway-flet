
import flet as ft
import matplotlib.pyplot as plt
import numpy as np

def main(page: ft.Page):
    page.title = "Project Cost Calculator"
    
    def calculate_project_cost(hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier):
        paid_hours = max(0, hours - pro_bono_hours)
        subsidized_hours = min(paid_hours, subsidized_hours)
        full_rate_hours = paid_hours - subsidized_hours

        discounted_rate = rate * (1 - discount_rate)
        cash_payment = (full_rate_hours * rate) + (subsidized_hours * discounted_rate)

        if valuation > 0 and total_shares > 0:
            equity_value_per_share = valuation / total_shares
            equity_value = (equity_split / 100) * hours * rate / equity_value_per_share
        else:
            equity_value = 0
        
        total_cost = (cash_payment + equity_value) * ip_multiplier
        return total_cost, cash_payment, equity_value

    def plot_project_cost():
        hours = hours_slider.value
        rate = rate_slider.value
        equity_split = equity_slider.value
        ip_ownership = ip_ownership_dropdown.value
        pro_bono_hours = pro_bono_slider.value
        subsidized_hours = subsidized_slider.value
        discount_rate = discount_slider.value
        valuation = valuation_slider.value
        total_shares = shares_slider.value
        
        ip_ownership_multipliers = {
            "Full IP Ownership": 1.0,
            "Joint IP Ownership": 0.9,
            "No IP Ownership": 0.8
        }
        ip_multiplier = ip_ownership_multipliers[ip_ownership]
        
        total_cost, cash_payment, equity_value = calculate_project_cost(
            hours, rate, equity_split, ip_ownership, pro_bono_hours, subsidized_hours, discount_rate, valuation, total_shares, ip_multiplier
        )

        # Plotting
        labels = ['Cash Payment', 'Equity Value']
        values = [cash_payment, equity_value]
        
        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=['#ff9999','#66b3ff'])
        plt.title(f"Total Project Cost: ${total_cost:.2f}")
        plt.ylabel('Amount in $')
        
        plt_path = "/tmp/plot.png"
        plt.savefig(plt_path)
        plt.close()
        
        chart_image.src = plt_path
        chart_image.update()

    # Sliders
    hours_slider = ft.Slider(min=10, max=100, value=20, label="Hours", on_change=lambda _: plot_project_cost())
    rate_slider = ft.Slider(min=50, max=200, value=120, label="Hourly Rate ($)", on_change=lambda _: plot_project_cost())
    equity_slider = ft.Slider(min=0, max=100, value=50, label="Equity Split (%)", on_change=lambda _: plot_project_cost())
    pro_bono_slider = ft.Slider(min=0, max=40, value=8, label="Pro Bono Hours", on_change=lambda _: plot_project_cost())
    subsidized_slider = ft.Slider(min=0, max=40, value=8, label="Subsidized Hours", on_change=lambda _: plot_project_cost())
    discount_slider = ft.Slider(min=0, max=0.5, value=0.1, label="Discount (%)", on_change=lambda _: plot_project_cost())

    # Dropdown for IP Ownership
    ip_ownership_dropdown = ft.Dropdown(
        label="IP Ownership",
        options=[
            ft.dropdown.Option("Full IP Ownership"),
            ft.dropdown.Option("Joint IP Ownership"),
            ft.dropdown.Option("No IP Ownership"),
        ],
        value="Full IP Ownership",
        on_change=lambda _: plot_project_cost()
    )

    # Sliders for valuation and shares
    valuation_slider = ft.Slider(min=100000, max=10000000, value=1000000, label="Valuation ($)", on_change=lambda _: plot_project_cost())
    shares_slider = ft.Slider(min=1000, max=1000000, value=100000, label="Total Shares", on_change=lambda _: plot_project_cost())

    # Image for the bar chart
    chart_image = ft.Image()

    # Adding controls to the page
    page.add(
        hours_slider,
        rate_slider,
        equity_slider,
        ip_ownership_dropdown,
        pro_bono_slider,
        subsidized_slider,
        discount_slider,
        valuation_slider,
        shares_slider,
        chart_image,
    )

    # Initial plot
    plot_project_cost()

# Run the app
ft.app(target=main)



# import logging
# import flet as ft
# import os


# import flet as ft

# # Define the descriptions for each principle
# descriptions = {
#     'Protect': 'Protect: Shielding from triggers helps manage stress.',
#     'Personalize': 'Personalize: Tailoring interventions to individual needs is crucial.',
#     'Gradual Exposure': 'Gradual Exposure: Slowly introducing challenges helps build resilience.',
#     'Empower': 'Empower: Providing control and choice boosts confidence and skill development.'
# }

# def main(page: ft.Page):
#     # Initial description
#     description = ft.Text(value="", size=20, weight="bold", color=ft.colors.RED)

#     # Function to update description based on clicked principle
#     def update_description(principle):
#         description.value = descriptions[principle]
#         page.update()

#     # Create the circular graphic (simple representation with buttons)
#     graphic = ft.Row(
#         controls=[
#             ft.Column(
#                 controls=[
#                     ft.ElevatedButton("Protect", on_click=lambda _: update_description('Protect')),
#                     ft.ElevatedButton("Personalize", on_click=lambda _: update_description('Personalize')),
#                     ft.ElevatedButton("Gradual Exposure", on_click=lambda _: update_description('Gradual Exposure')),
#                     ft.ElevatedButton("Empower", on_click=lambda _: update_description('Empower')),
#                 ],
#                 alignment="center"
#             )
#         ],
#         alignment="center"
#     )

#     page.add(graphic)
#     page.add(description)

# # Run the app
# # ft.app(target=main)


# ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
