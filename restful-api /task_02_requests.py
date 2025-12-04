import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder API and prints their titles
    """
    # API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request
    response = requests.get(url)
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Print all post titles
        for post in posts:
            print(post['title'])
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder API and saves them to a CSV file
    """
    # API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Structure data into list of dictionaries
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define fieldnames (column headers)
            fieldnames = ['id', 'title', 'body']
            
            # Create CSV writer
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write all posts
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")
        print(f"Total posts saved: {len(structured_posts)}")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

# Test the functions
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
