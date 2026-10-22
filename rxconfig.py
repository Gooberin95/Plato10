import reflex as rx

config = rx.Config(
    app_name="portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="mint",
                gray_color="sage",
                radius="medium",
                has_background=False,
                panel_background="translucent",
            )
        ),
    ],
)
