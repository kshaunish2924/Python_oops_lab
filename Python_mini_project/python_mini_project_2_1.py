import requests
import tkinter as tk
from tkinter import messagebox

def fetch_news(api_key, keyword, num_headlines=5):
    url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&language=en&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        if data["status"] == "ok":
            articles = data["articles"][:num_headlines]
            display_news(articles)
        else:
            messagebox.showerror("Error", f"Error fetching news: {data['message']}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_news(articles):
    # Clear the output text box
    output_text.delete(1.0, tk.END)
    
    # Display articles in the text box
    for i, article in enumerate(articles, start=1):
        title = article['title']
        description = article.get('description', 'No description available.')
        url = article['url']
        
        output_text.insert(tk.END, f"{i}. {title}\n")
        output_text.insert(tk.END, f"   Description: {description}\n")
        output_text.insert(tk.END, f"   URL: {url}\n\n")

def on_fetch_button_click():
    keyword = entry_keyword.get()
    if not keyword:
        messagebox.showwarning("Input Required", "Please enter a keyword to fetch news.")
        return
    fetch_news(api_key, keyword)

# Replace 'your_api_key' with your actual NewsAPI key
api_key = "e76d3417701d4eb29838fe3c61a7e379"  

# Create the main window
root = tk.Tk()
root.title("News Fetcher")

# Create and place the keyword label and entry box
label_keyword = tk.Label(root, text="Enter a keyword:")
label_keyword.pack(pady=10)

entry_keyword = tk.Entry(root, width=50)
entry_keyword.pack(pady=10)

# Create and place the "Fetch News" button
fetch_button = tk.Button(root, text="Fetch News", command=on_fetch_button_click)
fetch_button.pack(pady=20)

# Create a Text widget to display news results
output_text = tk.Text(root, height=15, width=80)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
