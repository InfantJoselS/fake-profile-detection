import tkinter as tk
from tkinter import messagebox

# Function to detect fake Snapchat accounts
def is_fake_snapchat_account(username, followers, snap_score):
    fake_score = 0
    
    # Rule 1: If the account has very low followers
    if followers < 10:
        fake_score += 3  

    # Rule 2: High snap score with low followers (possible bot)
    if snap_score > 10000 and followers < 20:
        fake_score += 4  

    # Rule 3: Suspicious username patterns (too simple or generic)
    if "snap" in username.lower() or username.isnumeric():
        fake_score += 2  

    # If fake_score >= 5, it's likely fake
    return fake_score >= 5  

# Function to check the account based on user input
def check_account():
    username = entry_username.get().strip()
    
    # Ensure numbers are entered correctly
    try:
        followers = int(entry_followers.get().strip())
        snap_score = int(entry_snapscore.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for Followers and Snap Score!")
        return

    # Fake account detection
    fake = is_fake_snapchat_account(username, followers, snap_score)
    result = "❌ Fake Account" if fake else "✅ Genuine Account"

    messagebox.showinfo("Snapchat Account Analysis", 
                        f"👤 Username: {username}\n"
                        f"👥 Followers: {followers}\n"
                        f"🔥 Snap Score: {snap_score}\n\n"
                        f"🔍 Result: {result}")

# GUI Setup
root = tk.Tk()
root.title("Snapchat Fake Account Detector")
root.geometry("400x300")
root.configure(bg="#fffcf5")  # Light background

# Labels and Input Fields
tk.Label(root, text="Enter Snapchat Username:", font=("Arial", 12, "bold"), bg="#fffcf5").pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.pack(pady=5)

tk.Label(root, text="Enter Number of Followers:", font=("Arial", 12, "bold"), bg="#fffcf5").pack(pady=5)
entry_followers = tk.Entry(root, font=("Arial", 12))
entry_followers.pack(pady=5)

tk.Label(root, text="Enter Snap Score:", font=("Arial", 12, "bold"), bg="#fffcf5").pack(pady=5)
entry_snapscore = tk.Entry(root, font=("Arial", 12))
entry_snapscore.pack(pady=5)

# Check Button
tk.Button(root, text="Check Account", command=check_account, font=("Arial", 12, "bold"), bg="#ff6600", fg="white", padx=10, pady=5).pack(pady=20)

root.mainloop()