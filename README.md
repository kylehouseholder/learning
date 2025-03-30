# Learning Projects

This repository contains my learning projects for Rust and Python.

## Project Structure
- `rust/` - Rust learning projects (including Rustlings)
- `python/` - Python learning projects

## Setup Instructions

### Initial Setup (One-time per device)
1. Generate an SSH key (if you don't already have one):
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```

2. Add the SSH key to GitHub:
   - Display your public key: `cat ~/.ssh/id_ed25519.pub`
   - Copy the output
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste the key and give it a name to identify this device

3. Clone this repository:
   ```bash
   git clone git@github.com:YOUR_USERNAME/learning.git
   ```

4. Configure Git on the device:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

5. For Rust projects:
   - Install Rust and Rustlings on each device
   - Run `rustlings watch` in the rust directory to start learning

6. For Python projects:
   - Install Python on each device
   - Create and activate virtual environments as needed

### Daily Workflow
1. Before starting work:
   ```bash
   git pull origin main
   ```

2. After completing exercises:
   ```bash
   git add .
   git commit -m "Completed: [Exercise Name]"
   git push origin main
   ```

## Notes
- Always pull before starting work to get the latest changes
- Commit frequently with descriptive messages
- Push changes when you're done working
- Each device should have its own unique SSH key for security
