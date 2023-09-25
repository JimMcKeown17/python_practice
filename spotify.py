playlist = {
    'title': 'patagonia bus',
    'author': 'qhawe',
    'songs': [{'title': 'song', 'artist': ['blue'], 'duration': 30.5},
              {'title': 'song2', 'artist': ['blue'], 'duration': 30.5},
              {'title': 'song3', 'artist': ['blue'], 'duration': 30.5},
]
}
duration = 0
for song in playlist['songs']:
    duration += song["duration"]

print(duration)