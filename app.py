from flask import Flask, render_template, send_file
import random
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Simulate getting the last 20 crash multipliers
def get_recent_crashes():
    return [round(random.uniform(1.0, 100.0), 2) for _ in range(20)]

# Generate chart
def create_chart(data):
    plt.figure(figsize=(10, 4))
    plt.plot(data, marker='o', linestyle='-', color='blue')
    plt.title('Aviator Crash Multiplier History')
    plt.xlabel('Game Number')
    plt.ylabel('Multiplier (x)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('static/chart.png')
    plt.close()

@app.route('/')
def home():
    data = get_recent_crashes()
    create_chart(data)
    return render_template('index.html', data=data)

@app.route('/chart')
def chart():
    return send_file('static/chart.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
