import random
import pandas as pd

# Создание базы данных треков
tracks_data = {
    'track_name': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E'],
    'artist': ['Artist 1', 'Artist 2', 'Artist 1', 'Artist 3', 'Artist 2'],
    'genre': ['Pop', 'Rock', 'Pop', 'Jazz', 'Rock']
}

tracks_df = pd.DataFrame(tracks_data)

def play_track(track_name):
    print(f"Playing: {track_name}")

def recommend_tracks(current_track):
    # Найдем жанр текущего трека
    genre = tracks_df.loc[tracks_df['track_name'] == current_track, 'genre'].values[0]
    
    # Рекомендуем треки из того же жанра
    recommendations = tracks_df[tracks_df['genre'] == genre]['track_name'].tolist()
    recommendations.remove(current_track)  # Убираем текущий трек
    return random.sample(recommendations, min(len(recommendations), 2))  # Рекомендуем 2 трека

def main():
    print("Welcome to the Music Player!")
    print("Available tracks:")
    
    for index, row in tracks_df.iterrows():
        print(f"{index + 1}. {row['track_name']} by {row['artist']} - Genre: {row['genre']}")
    
    while True:
        choice = input("Enter the track number to play (or 'exit' to quit): ")
        
        if choice.lower() == 'exit':
            print("Exiting the player. Goodbye!")
            break
        
        try:
            track_number = int(choice) - 1
            if 0 <= track_number < len(tracks_df):
                current_track = tracks_df.iloc[track_number]['track_name']
                play_track(current_track)
                recommendations = recommend_tracks(current_track)
                print(f"We recommend you to listen to: {', '.join(recommendations)}")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
































































































