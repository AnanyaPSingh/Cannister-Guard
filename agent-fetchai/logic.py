import subprocess
import json
import re
import os

def get_canister_status_message() -> str:
    """
    This function fetches the local canister's actual status from the local ICP network
    and formats a success message. It automatically gets the canister ID from the local deployment.
    """
    try:
        # Get the canister ID from the local deployment
        canister_ids_path = "../backend-icp/canister_guard/.dfx/local/canister_ids.json"
        
        if not os.path.exists(canister_ids_path):
            return "❌ **Error**: Cannot find local canister deployment. Make sure the backend is deployed locally."
        
        with open(canister_ids_path, 'r') as f:
            canister_ids = json.load(f)
        
        backend_canister_id = canister_ids.get("canister_guard_backend", {}).get("local")
        
        if not backend_canister_id:
            return "❌ **Error**: Cannot find local backend canister ID."
        
        print(f"Logic: Fetching status for local backend canister {backend_canister_id}")

        # Call the local canister using dfx from the backend directory
        backend_dir = "../backend-icp/canister_guard"
        result = subprocess.run([
            'dfx', 'canister', 'call', 'canister_guard_backend', 'get_status', 
            f'("{backend_canister_id}")'
        ], capture_output=True, text=True, check=True, cwd=backend_dir)
        
        # Parse the dfx output
        output = result.stdout.strip()
        print(f"Raw dfx output: {output}")
        
        # Extract the status data using regex
        # The output format is: (opt record { status = "running"; memory_size = 5_522_147 : nat; cycles = 2_916_126_801_212 : nat; },)
        status_match = re.search(r'status = "([^"]+)"', output)
        memory_match = re.search(r'memory_size = ([0-9_]+)', output)
        cycles_match = re.search(r'cycles = ([0-9_]+)', output)
        
        if not all([status_match, memory_match, cycles_match]):
            return f"❌ **Error**: Could not parse canister status for `{backend_canister_id[:5]}...`"
        
        # Extract and convert values
        status = status_match.group(1)
        memory_size = int(memory_match.group(1).replace('_', ''))
        cycles = int(cycles_match.group(1).replace('_', ''))
        
        # Format the response into a clean, user-friendly message
        formatted_message = (
            f"✅ **Status for local backend canister `{backend_canister_id[:5]}...`**:\n"
            f"- **Status:** {status.capitalize()}\n"
            f"- **Cycle Balance:** {cycles:,}\n"
            f"- **Memory Size:** {memory_size / 1024:,.2f} KiB"
        )
        
        return formatted_message
        
    except subprocess.CalledProcessError as e:
        print(f"Error calling dfx: {e}")
        print(f"stderr: {e.stderr}")
        return "❌ **Error**: Failed to fetch status. Make sure the canister is running locally."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "❌ **Error**: Unexpected error while fetching status."

# Example of how to test your function directly
if __name__ == '__main__':
    message = get_canister_status_message()
    print("--- Your function generated this message: ---")
    print(message)
