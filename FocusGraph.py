import matplotlib.pyplot as plt

def generate_graph():
    try:
        with open("focus.txt", "r") as file:
            content = file.readlines()
        
        # Convert each line to a float and strip any newline characters
        focus_times = [float(line.strip()) for line in content]
        
        # Generate x-axis values based on the number of focus times recorded
        x_values = list(range(1, len(focus_times) + 1))

        # Plot the focus times
        plt.plot(x_values, focus_times, color="red", marker="o")
        
        # Add title and labels
        plt.title("YOUR FOCUSED TIME", fontsize=16)
        plt.xlabel("Session Number", fontsize=14)
        plt.ylabel("Focus Time (hours)", fontsize=14)
        
        # Enable grid for better readability
        plt.grid(True)
        
        # Display the plot
        plt.show()

    except FileNotFoundError:
        print("No focus data available to plot.")
    except ValueError:
        print("Error reading focus data.")

# Call the function to display the graph
generate_graph()
