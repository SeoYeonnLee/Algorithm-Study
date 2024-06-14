def solution(genres, plays):
    N = len(genres)
    genre_cnt = {}
    genre_song = {}
    song_cnt = {}
    album = []
    
    for i in range(N):
        genre_cnt[genres[i]] = genre_cnt.get(genres[i], 0) + plays[i]
        
        if genres[i] in genre_song:
            genre_song[genres[i]].append(i)
        else:
            genre_song[genres[i]] = [i]
        
        song_cnt[i] = plays[i]

    genres = sorted(genre_cnt, key=lambda x:genre_cnt[x], reverse=True)
    
    for genre in genres:
        high_song = sorted(genre_song[genre], key=lambda x: song_cnt[x], reverse=True)
        album.extend(high_song[:2])

    return album