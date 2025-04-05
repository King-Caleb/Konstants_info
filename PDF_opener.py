import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import pygame
import time

# Initialize Pygame
pygame.init()


class PDFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer App")

        # PDF Variables
        self.pdf_path = None
        self.pages = []
        self.current_page = 0
        self.doc = None  # PyMuPDF document

        # Create Pygame window
        self.canvas_width = 800
        self.canvas_height = 600
        self.screen = pygame.display.set_mode((1, 1))
        pygame.display.set_caption("PDF Viewer (Pygame)")

        # Tkinter UI Components
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.open_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        self.open_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.root, text="Next Page", command=self.next_page)
        self.next_button.pack(side=tk.LEFT)

        self.prev_button = tk.Button(self.root, text="Previous Page", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT)

        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(self.root, text="Save", command=self.save)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.save_as_button = tk.Button(self.root, text="Save As", command=self.save_as)
        self.save_as_button.pack(side=tk.LEFT, padx=5)

        self.enter_text_button = tk.Button(self.root, text="Enter Text", command=self.add_text)
        self.enter_text_button.pack(side=tk.LEFT, padx=5)

        self.eraser_mode = False
        self.dragging = False  # Track if user is dragging
        self.start_x = None
        self.start_y = None

        # Bind mouse events for erasing
        self.canvas.bind("<ButtonPress-1>", self.start_erase)
        self.canvas.bind("<B1-Motion>", self.do_erase)
        self.canvas.bind("<ButtonRelease-1>", self.end_erase)

        # To prevent garbage collection of the image
        self.tk_image = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path = file_path
            self.doc = fitz.open(file_path)
            self.pages = self.convert_pdf_to_images()
            self.display_page(self.current_page)

    def convert_pdf_to_images(self):
        images = []
        for page in self.doc:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        return images

    def add_text(self):
        """Allows user to place and move text dynamically on the PDF."""
        if not self.doc or self.current_page < 0:
            return

        popup = tk.Toplevel(self.root)
        popup.title("Enter Text")

        tk.Label(popup, text="Enter text:").pack(pady=5)
        text_entry = tk.Entry(popup, font=("Arial", 14))
        text_entry.pack(pady=5)

        def start_text_placement():
            user_text = text_entry.get()
            if not user_text.strip():
                return

            popup.destroy()
            text_x, text_y = 200, 200
            text_id = self.canvas.create_text(text_x, text_y, text="", font=("Arial", 20), fill="red")

            for char in user_text:
                current_text = self.canvas.itemcget(text_id, "text")
                self.canvas.itemconfig(text_id, text=current_text + char)
                self.root.update()
                time.sleep(0.1)

            def move_text(event):
                self.canvas.coords(text_id, event.x, event.y)

            def place_text(event):
                self.canvas.unbind("<B1-Motion>")
                self.canvas.unbind("<ButtonRelease-1>")
                final_x, final_y = event.x, event.y
                page = self.doc[self.current_page]
                page.insert_text((final_x, final_y), user_text, fontsize=20, color=(1, 0, 0))
                self.pages[self.current_page] = self.render_page(self.current_page)
                self.display_page(self.current_page)

            self.canvas.bind("<B1-Motion>", move_text)
            self.canvas.bind("<ButtonRelease-1>", place_text)

        tk.Button(popup, text="Place Text", command=start_text_placement).pack(pady=5)
        popup.mainloop()

    def display_page(self, page_num):
        if 0 <= page_num < len(self.pages):
            img = self.pages[page_num]
            self.tk_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.display_page(self.current_page)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page(self.current_page)

    def save(self):
        """Saves the current PDF with modifications."""
        if self.doc:
            self.doc.save(self.pdf_path)  # Save changes
            print("PDF saved successfully!")

    def save_as(self):
        """Saves the PDF with modifications to a new file."""
        if self.doc:
            new_file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                         filetypes=[("PDF files", "*.pdf")])
            if new_file_path:
                self.doc.save(new_file_path)
                print(f"PDF saved successfully to: {new_file_path}")

    def toggle_eraser(self):
        if self.eraser_mode:
            self.eraser_mode = False
            print(f"Eraser mode: {'ON' if self.eraser_mode else 'OFF'}")
        else:
            self.eraser_mode = True

    def start_erase(self, event):
        """Start erasing when the user clicks the mouse."""
        if self.eraser_mode:
            self.dragging = True
            self.erase_text(event.x, event.y)

    def do_erase(self, event):
        """Erase while dragging the mouse."""
        if self.eraser_mode and self.dragging:
            self.erase_text(event.x, event.y)

    def end_erase(self, event):
        """Stop erasing when the mouse is released."""
        if self.eraser_mode:
            self.dragging = False
            self.display_page(self.current_page)  # Refresh page after erasing

    def erase_text(self, x, y):
        """Erase text by drawing a white rectangle over the specified area."""
        if not self.doc or self.current_page < 0:
            return

        page = self.doc[self.current_page]

        # Define a small rectangle around the (x, y) position
        erase_rect = fitz.Rect(x - 10, y - 10, x + 10, y + 10)

        # Draw a white rectangle over the area
        page.draw_rect(erase_rect, color=(1, 1, 1), fill=(1, 1, 1))

        # Re-render and display the updated page
        self.pages[self.current_page] = self.render_page(self.current_page)
        self.display_page(self.current_page)

    def render_page(self, page_num):
        page = self.doc.load_page(page_num)
        pix = page.get_pixmap()
        return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


root = tk.Tk()
app = PDFViewerApp(root)
root.mainloop()
