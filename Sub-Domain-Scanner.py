from bs4 import BeautifulSoup
import requests
import subprocess
import urllib.parse

def find_directory(url):


    data_got = requests.get(url)
    print(data_got)

    soup = BeautifulSoup(data_got.text, 'html.parser')


    links = soup.find_all('a')

  
    for link in links:
        href = link.get('href')  
        if href:  
            print(href)



def deep_directory(deep_link):
    visited_urls = set()  

    def crawl(deep_link):
        if deep_link in visited_urls:
            return  # Avoid infinite loops
        visited_urls.add(deep_link)

        try:
            response = requests.get(deep_link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                print("Current URL:", deep_link)

                # Find all links on the page
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        absolute_url = urllib.parse.urljoin(deep_link, href)  # Resolve relative URLs
                        print("Found link:", absolute_url)
                        crawl(absolute_url)  # Recursively crawl the new URL
        except Exception as e:
            print(f"Error crawling {deep_link}: {e}")

    crawl(deep_link)

print("/////////////////////////////////------CYBER SECURITY TOOL------////////////////////////////////////")
print("//  ___________       __         __      _____________         ___________      _____________     //                          ")
print("// |   ________|      \\ \\       / /      | |_________  |      |  __________|    | __________  |   //            ")
print("// |  |                \\ \\     / /       | |         | |      | |               | |         | |   //            ")
print("// |  |                 \\ \\   / /        | |         | |      | |               | |         | |   //            ")
print("// |  |                  \\ \\ / /         | |_________| |      | |__________     | |_________| |   //            ")
print("// |  |                    | |           | |_________  |      |  __________|    | |______  ___|   //          ")
print("// |  |                    | |           | |         | |      | |               | |      \\ \\      //            ")
print("// |  |                    | |           | |         | |      | |               | |       \\ \\     //            ")
print("// |  |________            | |           | |_________| |      | |__________     | |        \\ \\    //            ")
print("// |___________|           |_|           | |___________|      |  __________|    |_|         \\_\\   //            ")
print("////////////////////////////////////////////////////////////////////////////////////////////////////               ")  
i = 1

if i<= 1:
    print(" ")
    i = i+1





option_list = ["1. Find SubDirectory",
               "2. CyberTool Description",
               "3. Install Needed Module",
               "4. Directory Thread Scan"]

for items in option_list:
    print(items)
    print(" ")
option_number = int(input("Select one valid option[]: "))   




if option_number == 1:
    url = input("Enter a valid link: ")
    find_directory(url)

elif option_number == 2:

    
    print("\n")
    Description = [
        "////////////-----Welcome To CyberTool!------/////////////\n",

        "_______Directory Enumeration:________\n",
        "Our tool performs thorough directory enumeration ",
        "by parsing the HTML content of the provided URL",
        "and extracting directory URLs.\n",

        "______Hidden Directory Detection:______\n",
        "In addition to standard directories, our tool can",
        "also identify hidden directories embedded within",
        "HTML, JavaScript, or CSS files.",
    ]
    for descrip in Description:
        print(descrip)  



elif option_number == 3:
    print(" ")
    print("##You can enter the following command and install the modules##\n")
    print("1* sudo apt install python3-requests")
    print("2* sudo apt install python3-bs4")
    print("3* pip3 install beautifulsoup4\n")
    auto = input("Or To Install Automatically Enter (yes): ")
    auto_command = auto.lower()

    if auto_command == "yes":
        print("Enter 1. Auto Installation For KALI LINUX")
        print("Enter 2. Auto Installation For MAC",)

        option_value = int(input("enter the valid options: "))
        if option_value == 1:





            def install_requests():
                try:
                    subprocess.run(["sudo", "apt", "install", "python3-requests"], check=True)
                    print("requests installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install requests: {e}")

            def install_bs4():
                try:
                    
                    subprocess.run(["sudo", "apt", "install", "python3-bs4"], check=True)
                    print("bs4 installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install bs4: {e}")

            def install_beautifulsoup4():
                try:
                    
                    subprocess.run(["pip3", "install", "beautifulsoup4"], check=True)
                    print("beautifulsoup4 installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install beautifulsoup4: {e}")  

            if __name__ == "__main__":
                install_requests()
                install_bs4()
                install_beautifulsoup4()




        elif option_value == 2:
            print("mac installtion")




            def install_mac_requests():
                try:
                    subprocess.run(["pip3", "install", "requests"], check=True)
                    print("requests installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install requests: {e}")

            def install_mac_bs4():
                try:
                    
                    subprocess.run(["pip3", "install", "bs4"], check=True)
                    print("bs4 installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install bs4: {e}")

            def install_mac_beautifulsoup4():
                try:
                    
                    subprocess.run(["pip3", "install", "beautifulsoup4"], check=True)
                    print("beautifulsoup4 installed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: Failed to install beautifulsoup4: {e}")
            if __name__ == "__main__":
                install_mac_requests()
                install_mac_bs4()
                install_mac_beautifulsoup4()
    else:
        exit("you did not entered yes...try manual installation")

elif option_number == 4:
    deep_link = input("Enter Url For Thread Scan:")
    deep_directory(deep_link)


else:
    print("Invalid Option...Try Again")
        
