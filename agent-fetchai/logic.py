def get_canister_status_message(canister_id: str) -> str:
    """
    This function simulates fetching a canister's status and formats a success message.
    For now, it uses hardcoded mock data.
    """
    print(f"Logic: Pretending to fetch status for {canister_id}")

    # MOCK DATA: This is a placeholder for the real data from the canister.
    mock_response = {
        'status': 'running',
        'cycles': 5_123_456_789_012,  # Using underscores for readability
        'memory_size': 123456
    }

    # Format the response into a clean, user-friendly message (ChatProtocol style)
    formatted_message = (
        f"✅ **Status for canister `{canister_id[:5]}...`**:\n"
        f"- **Status:** {mock_response['status'].capitalize()}\n"
        f"- **Cycle Balance:** {mock_response['cycles']:,}\n"
        f"- **Memory Size:** {mock_response['memory_size'] / 1024:,.2f} KiB"
    )
    return formatted_message

# Example of how to test your function directly
if __name__ == '__main__':
    test_id = "rrkah-fqaaa-aaaaa-aaaaq-cai"
    message = get_canister_status_message(test_id)
    print("--- Your function generated this message: ---")
    print(message)
