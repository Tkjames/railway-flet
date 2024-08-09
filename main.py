import logging
import flet as ft
import os


import flet as ft

# Define the descriptions for each principle
descriptions = {
    'Protect': 'Protect: Shielding from triggers helps manage stress.',
    'Personalize': 'Personalize: Tailoring interventions to individual needs is crucial.',
    'Gradual Exposure': 'Gradual Exposure: Slowly introducing challenges helps build resilience.',
    'Empower': 'Empower: Providing control and choice boosts confidence and skill development.'
}

def main(page: ft.Page):
    # Initial description
    description = ft.Text(value="", size=20, weight="bold", color=ft.colors.BLACK)

    # Function to update description based on clicked principle
    def update_description(principle):
        description.value = descriptions[principle]
        page.update()

    # Create the circular graphic (simple representation with buttons)
    graphic = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.ElevatedButton("Protect", on_click=lambda _: update_description('Protect')),
                    ft.ElevatedButton("Personalize", on_click=lambda _: update_description('Personalize')),
                    ft.ElevatedButton("Gradual Exposure", on_click=lambda _: update_description('Gradual Exposure')),
                    ft.ElevatedButton("Empower", on_click=lambda _: update_description('Empower')),
                ],
                alignment="center"
            )
        ],
        alignment="center"
    )

    page.add(graphic)
    page.add(description)

# Run the app
# ft.app(target=main)


ft.app(target=main, view=None, port=int(os.getenv("PORT", 8502)))
