from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class HistoricalStoryChatbot:
    def __init__(self):
        """
        Initialize the chatbot with historical events and story templates.
        """
        self.historical_events = {
            'World War II': [
                'In the heart of {location}, a {profession} discovers {secret} that could change the course of the war.',
                'Amidst the chaos of {battle}, {character} makes an unexpected {action} that alters history.',
                'A hidden resistance fighter in {location} risks everything to {mission}.'
            ],
            'Renaissance': [
                'In the vibrant streets of {city}, an artist named {character} uncovers a {mystery} that challenges everything.',
                'A merchant travels through {location}, carrying a {secret} that could revolutionize {field}.',
                'During a grand {event}, {character} makes a discovery that will reshape {domain}.'
            ],
            'Ancient Egypt': [
                'In the shadow of the pyramids, a {role} named {character} embarks on a journey to {quest}.',
                'A secret scroll reveals a {mystery} that could change the understanding of {subject}.',
                'During the reign of {pharaoh}, an unexpected {event} transforms {location}.'
            ]
        }

    def generate_story(self, event: str) -> str:
        """
        Generate a random story for a given historical event.
        """
        if event not in self.historical_events:
            return "Sorry, I don't have a story for that historical event."
        
        story_templates = self.historical_events[event]
        story_template = random.choice(story_templates)
        
        # Fill in placeholders with random details
        story = story_template.format(
            location=random.choice(['Paris', 'London', 'Berlin', 'Rome', 'Cairo']),
            profession=random.choice(['soldier', 'spy', 'journalist', 'scientist', 'artist']),
            secret=random.choice(['a hidden document', 'a mysterious artifact', 'a coded message']),
            battle=random.choice(['D-Day', 'Battle of Britain', 'Battle of Stalingrad']),
            character=random.choice(['Elena', 'Marcus', 'Sofia', 'Jack', 'Isabella']),
            action=random.choice(['heroic rescue', 'unexpected alliance', 'critical decision']),
            mission=random.choice(['save a village', 'protect refugees', 'sabotage enemy plans']),
            city=random.choice(['Florence', 'Venice', 'Milan', 'Rome']),
            mystery=random.choice(['lost artwork', 'family secret', 'hidden invention']),
            field=random.choice(['art', 'science', 'trade', 'politics']),
            event=random.choice(['Medici ball', 'art exhibition', 'merchant gathering']),
            domain=random.choice(['art world', 'scientific community', 'political landscape']),
            role=random.choice(['scribe', 'priest', 'merchant', 'craftsman']),
            quest=random.choice(['uncover a conspiracy', 'find a lost treasure', 'solve an ancient riddle']),
            subject=random.choice(['astronomy', 'architecture', 'medicine']),
            pharaoh=random.choice(['Ramesses II', 'Tutankhamun', 'Cleopatra'])
        )
        
        return story

chatbot = HistoricalStoryChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    user_input = request.form.get('event', '')
    
    if user_input:
        story = chatbot.generate_story(user_input)
        return jsonify({
            'userMessage': user_input,
            'botMessage': story
        })
    
    return jsonify({
        'userMessage': '',
        'botMessage': 'Please enter a historical event like World War II, Renaissance, or Ancient Egypt.'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
