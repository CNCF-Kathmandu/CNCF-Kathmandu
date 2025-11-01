from string import Template

def mock_send_email(email: str, content: str ) -> None:
    print(f"Sending Mock Email to {email} with content {content}")


async def send_welcome_email(email:str, name: str ) -> None:
    welcome_content_html = Template(""" \
        <p> Dear $name,
        <h1> Thank You for contacting us </h1>
        <p> We want to take this moment to thank you for your contact, we will get back to you soon! </p>
        <p> - CNCF Kathmandu </p>
    """)

    welcome_content = welcome_content_html.safe_substitute({
        "name": name
    })

    await mock_send_email(email=email, content=welcome_content)

