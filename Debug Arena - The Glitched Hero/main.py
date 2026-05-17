from game.game import Game 
def start_game():
    print(">>> Oyun Motoru Hazırlanıyor...")
    try:
        #oyun motorunu başlatıyoruz
        game=Game()
        game.start()
    except Exception as e:
     print(f"Oyun başlatılırken bir hata oluştu:{e}")
    
if __name__ == "__main__":
        start_game()