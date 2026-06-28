from core.orchestrator import run

from feedback.feedback_processor import get_feedback
from feedback.regenerate import regenerate_content


def main():

    # User Topic
    topic = input("Enter Topic: ")

    # Generate Content
    content, validations = run(topic)

    print("\n")
    print("=" * 60)
    print("GENERATED PLATFORM CONTENT")
    print("=" * 60)

    # Display content for each platform
    for platform, post in content.items():

        print("\n")
        print("=" * 60)
        print(platform.upper())
        print("=" * 60)

        print(post)

    # Validation Results
    print("\n")
    print("=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    for platform, issues in validations.items():

        if issues:
            print(f"\n{platform.upper()}: FAILED")

            for issue in issues:
                print(f" - {issue}")

        else:
            print(f"\n{platform.upper()}: PASSED")

    # Feedback Section
    feedback = get_feedback()

    if feedback:

        regenerated = regenerate_content(
            topic,
            feedback
        )

        print("\n")
        print("=" * 60)
        print("REGENERATED CONTENT")
        print("=" * 60)

        print("\nARTICLE")
        print("-" * 60)
        print(regenerated["article"])

        print("\nCAPTION")
        print("-" * 60)
        print(regenerated["caption"])

        print("\nHASHTAGS")
        print("-" * 60)
        print(regenerated["hashtags"])


if __name__ == "__main__":
    main()