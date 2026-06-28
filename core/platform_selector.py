AVAILABLE_PLATFORMS = [
    "linkedin",
    "reddit",
    "facebook",
    "instagram",
    "twitter",
    "bluesky",
    "threads",
    "telegram"
]


def select_platforms():

    print("\nSelect platforms to publish:")
    print("--------------------------------")

    for i, platform in enumerate(AVAILABLE_PLATFORMS, start=1):
        print(f"{i}. {platform.title()}")

    choice = input(
        "\nEnter platform numbers separated by commas (Example: 1,3,5): "
    )

    selected = []

    try:

        indexes = [
            int(x.strip())
            for x in choice.split(",")
        ]

        for index in indexes:

            if 1 <= index <= len(AVAILABLE_PLATFORMS):
                selected.append(
                    AVAILABLE_PLATFORMS[index - 1]
                )

    except Exception:
        print("Invalid selection.")

    return selected