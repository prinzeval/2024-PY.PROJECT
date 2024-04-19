from flask import Flask, request, jsonify
from flask.cli import AppGroup
from models import db, Episode  # Assuming Episode is the SQLAlchemy model for episodes

# Create a Flask app
app = Flask(__name__)

# Define a Flask CLI command group
episode_cli = AppGroup('episode')

# Define the command to handle episode input
@episode_cli.command('add')
def add_episode():
    # Parse input data from HTML form
    title = request.form.get('title')
    episode_number = request.form.get('episode_number')
    # Parse other input fields as needed

    # Create a new Episode object
    episode = Episode(title=title, episode_number=episode_number)
    # Add the episode to the database session
    db.session.add(episode)
    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Episode added successfully'})

# Register the CLI command group with the Flask app
app.cli.add_command(episode_cli)

if __name__ == '__main__':
    app.run(debug=True)
