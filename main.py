from nicegui import ui
from rag import rag, llm
import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('data/feedback.db')

# Create a table for storing questions, responses, and feedback
conn.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        response TEXT NOT NULL,
        feedback TEXT
    )
''')
conn.commit()
conn.close()

dropdown_button = 'Select a model'

def save_to_db(question, response, feedback=None):
    conn = sqlite3.connect('data/feedback.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (question, response, feedback) VALUES (?, ?, ?)', (question, response, feedback))
    conn.commit()
    conn.close()

def save_feedback(question, response, feedback):
    conn = sqlite3.connect('data/feedback.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE feedback SET feedback = ? WHERE question = ? AND response = ?', (feedback, question, response))
    conn.commit()
    conn.close()
    ui.notify('Thank you for your feedback!')

def send_button_click():
    if drop.text == 'Select a model':
        ui.notify('Please select a model first')
    elif prompt.value == '':
        ui.notify('Empty prompt')
    else:
        ui.notify('Fetching the results...')
        question = prompt.value
        result = rag(question, drop.text)

        # Save the question and response in the database
        save_to_db(question, result)

        ui.markdown(result)
        ui.label('Did you like the reply?') \
            .style('text-align: center;')
        with ui.button_group():
            ui.button('👍', on_click=lambda: save_feedback(question, result, '👍'))
            ui.button('👎', on_click=lambda: save_feedback(question, result, '👎'))
    ui.update()


ui.image('https://upload.wikimedia.org/wikipedia/commons/e/e8/Archlinux-logo-standard-version.png') \
    .style('width: 200px; display: block; margin-left: auto; margin-right: auto;')
ui.label('This bot will help you set up your Arch distribution or fix existing issues') \
    .style('display: block; margin-left: auto; margin-right: auto;')
drop = ui.dropdown_button(dropdown_button, auto_close=True) \
    .style('display: block; margin-left: auto; margin-right: auto;')
with drop:
    ui.item('qwen2', on_click=lambda: drop.set_text('qwen2'))
    ui.item('llama3.1', on_click=lambda: drop.set_text('llama3.1'))
    ui.item('zephyr', on_click=lambda: drop.set_text('zephyr'))
    ui.item('gpt-4o-mini', on_click=lambda: drop.set_text('gpt-4o-mini'))
prompt = ui.input(label='Arch Linux bot ', placeholder='Type your question here') \
    .style('width: 40%; display: block; margin-left: auto; margin-right: auto;')
ui.button('Send', on_click=lambda: send_button_click()) \
    .style('display: block; margin-left: auto; margin-right: auto;')

ui.run()
