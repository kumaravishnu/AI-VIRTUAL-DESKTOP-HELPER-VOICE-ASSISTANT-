import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def block_websites(host_path, redirect, website_list):
    try:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if f"{redirect} {website}" in content:
                    continue  # Skip if already blocked
                file.write(f"{redirect} {website}\n")
                print(f"Blocked: {website}")
    except Exception as e:
        print(f"Error blocking websites: {e}")

def unblock_websites(host_path, redirect, website_list):
    try:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            unblocked_any = False
            
            for line in content:
                if any(f"{redirect} {website}" in line for website in website_list):
                    print(f"Unblocked: {line.strip()}")
                    unblocked_any = True  # Set the flag
                else:
                    file.write(line)
            
            if unblocked_any:
                file.truncate()  # Truncate the file if any unblocking happened
                print("Websites are unblocked!")
            else:
                print("No websites were blocked.")
    except Exception as e:
        print(f"Error unblocking websites: {e}")

def main():
    if is_admin():
        current_time = datetime.datetime.now().strftime("%H:%M")
        stop_time = input("Enter stop time (example [10:10]): ")
        
        try:
            current_time_float = float(current_time.replace(":", "."))
            stop_time_float = float(stop_time.replace(":", "."))
            focus_time = round(stop_time_float - current_time_float, 3)
        except ValueError:
            print("Invalid time format. Please use [HH:MM] format.")
            return
        
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
        redirect = '127.0.0.1'
        
        print(f"Current time: {current_time}")
        website_list = [
            'www.facebook.com', 'm.facebook.com',
            'www.instagram.com', 'm.instagram.com',
            'www.twitter.com', 'm.twitter.com',
            'www.linkedin.com', 'm.linkedin.com',
            'www.snapchat.com', 'm.snapchat.com',
            'www.pinterest.com', 'm.pinterest.com',
            'www.tumblr.com', 'm.tumblr.com',
            'web.whatsapp.com', 'm.web.whatsapp.com',
            'www.youtube.com', 'm.youtube.com', 'youtube-nocookie.com',
            'www.quora.com',
            'www.amazon.com', 'm.amazon.com',
            'www.ebay.com', 'm.ebay.com',
            'www.alibaba.com', 'm.alibaba.com'
        ]
        
        if current_time < stop_time:
            block_websites(host_path, redirect, website_list)
            print("FOCUS MODE TURNED ON !!!")

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time >= stop_time:
                unblock_websites(host_path, redirect, website_list)
                with open("focus.txt", "a") as focus_file:
                    focus_file.write(f"{focus_time}\n")
                break
            time.sleep(60)  # Check every minute
    else:
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Error elevating to admin: {e}")

if __name__ == "__main__":
    main()
