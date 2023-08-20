import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def load_data(file_path, file_type):
    if file_type == 'csv':
        data = pd.read_csv(file_path)
    elif file_type == 'excel':
        data = pd.read_excel(file_path)
    elif file_type == 'sql':
        if db_connection is None:
            raise ValueError("Please provide a database connection string.")
        engine = create_engine(db_connection)
        query = "SELECT * FROM your_table_name"
        data = pd.read_sql(query, engine)
    else:
        raise ValueError("Unsupported file type.")

    return data


def preprocess_data(data):
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = identify_categorical_features(data)  # Assuming you have this function defined

    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    data[numerical_features] = imputer.fit_transform(data[numerical_features])

    # One-hot encode categorical features
    data = pd.get_dummies(data, columns=[feature for feature, _ in categorical_features])

    # Scale numerical features
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    return data

def identify_categorical_features(data):
    categorical_features = data.select_dtypes(include=['object']).columns
    binary_features = []

    for feature in categorical_features:
        unique_values = data[feature].nunique()
        if unique_values == 2:
            binary_features.append((feature, 'binary'))
        else:
            binary_features.append((feature, 'categorical'))

    return binary_features

from matplotlib.backends.backend_pdf import PdfPages
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define your data loading and preprocessing functions here

def create_scatter_plot(data, feature):
    fig = px.scatter(data, x=feature, y='Total', title=f'Scatter Plot of {feature}')
    return fig

def create_pie_plot(data, feature):
    feature_counts = data[feature].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(feature_counts, labels=feature_counts.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(f'Pie Plot of {feature}')
    plt.show()

def create_bar_plot(data, feature):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x=feature)
    plt.title(f'Bar Plot of {feature}')
    plt.xticks(rotation=45)
    plt.show()

def create_histogram(ax, data, feature):
    sns.histplot(data[feature], bins=20, kde=True, ax=ax)
    ax.set_title(f'Histogram of {feature}')
    plt.tight_layout()
    plt.show()

def create_box_plot(ax, data, feature):
    sns.boxplot(x=data[feature], ax=ax)
    ax.set_title(f'Box Plot of {feature}')
    plt.tight_layout()
    plt.show()

def create_visualizations_for_column(data, column_name):
    fig_histogram, ax_histogram = plt.subplots(figsize=(8, 6))
    create_histogram(ax_histogram, data, column_name)

    fig_box_plot, ax_box_plot = plt.subplots(figsize=(8, 6))
    create_box_plot(ax_box_plot, data, column_name)

    fig_scatter_plot = create_scatter_plot(data, column_name)
    fig_pie_plot = create_pie_plot(data, column_name)
    fig_bar_plot = create_bar_plot(data, column_name)

    figures = [fig_histogram, fig_box_plot, fig_pie_plot, fig_bar_plot]
    return figures, fig_scatter_plot  

def generate_summary(data):
    summary_text.delete("1.0", tk.END)  # Clear previous content

    num_rows, num_cols = data.shape
    summary = f"Number of rows: {num_rows}\nNumber of columns: {num_cols}\n\n"
    summary += "Columns:\n" + "\n".join(data.columns.tolist())

    summary_text.insert(tk.END, summary)

import tkinter as tk
from tkinter import ttk

def visualize_data():
    global preprocessed_data  # Declare preprocessed_data as a global variable
    # Load and preprocess data
    file_path = file_path_entry.get()
    file_type = file_type_combobox.get()
    data = load_data(file_path, file_type)
    preprocessed_data = preprocess_data(data)


    # Get the chosen column to visualize
    column_to_visualize = column_entry.get()

    # Generate all types of plots for the chosen column
    figures, _ = create_visualizations_for_column(preprocessed_data, column_to_visualize)
    
    # Display the generated plots in the second half of the window
    for fig in figures:
        canvas = FigureCanvasTkAgg(fig, master=visual_frame)
        canvas.get_tk_widget().pack()


# Create the main window
root = tk.Tk()
root.title("Automated EDA Tool")

# Create and position the input widgets in the first half of the window
input_frame = tk.Frame(root)
input_frame.pack(padx=20, pady=20)

file_path_label = tk.Label(input_frame, text="File Path:")
file_path_label.grid(row=0, column=0, sticky="w")
file_path_entry = tk.Entry(input_frame)
file_path_entry.grid(row=0, column=1, padx=10)

file_type_label = tk.Label(input_frame, text="File Type:")
file_type_label.grid(row=1, column=0, sticky="w")
file_type_combobox = ttk.Combobox(input_frame, values=["csv", "excel", "sql"])
file_type_combobox.grid(row=1, column=1, padx=10)

column_label = tk.Label(input_frame, text="Column to Visualize:")
column_label.grid(row=2, column=0, sticky="w")
column_entry = tk.Entry(input_frame)
column_entry.grid(row=2, column=1, padx=10)

visual_button = tk.Button(input_frame, text="Visualize", command=visualize_data)
visual_button.grid(row=3, columnspan=2, pady=10)

# Create and position a frame for summary and visualizations
summary_visual_frame = tk.Frame(root)
summary_visual_frame.pack(padx=20, pady=20)

# Define a variable to store preprocessed data
preprocessed_data = None  # Initialize with None

# Define a function to update preprocessed_data
def update_preprocessed_data():
    global preprocessed_data
    file_path = file_path_entry.get()
    file_type = file_type_combobox.get()
    data = load_data(file_path, file_type)
    preprocessed_data = preprocess_data(data)

# Add a summary button
summary_button = tk.Button(summary_visual_frame, text="Generate Summary", command=lambda: [update_preprocessed_data(), generate_summary(preprocessed_data)])
summary_button.pack()

# Add a text widget for displaying the summary
summary_text = tk.Text(summary_visual_frame, height=10, width=40)
summary_text.pack()

# Start the GUI event loop
root.mainloop()