def preview_content(platform_content):

    print("\n")
    print("=" * 70)
    print("CONTENT PREVIEW")
    print("=" * 70)

    for platform, content in platform_content.items():

        print(f"\n{platform.upper()}")
        print("-" * 70)

        print(content)