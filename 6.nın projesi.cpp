#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;
// Abstract Player class
class Player{
    protected:
    string name;
    int score;
    string move;

public:
    Player(string playerName): name (playerName),score(0){}
    virtual~Player(){}
    string getName(){
        return name; 
        }
int getScore(){
    return score;
}
string getMove(){
    return move;
}
virtual void makeMove()= 0; // Abstract method 
void updateScore(string result){
    if (result== "win"){
    score++;
    }

   }
  };
// HumanPlayer class
class HumanPlayer : Player public 
    public:
   HumanPlayer(string playerName):Player(playerName){}
   void makeMove() override{
    cout << name <<",secim yapin: Tas(T),Kagit(K),Makas(M):";
    char choice;
    cin >> choice;
    choice = toupper(choice);

    while(choice!= 'T' && choice!='K' && choice!='M'){
        cout << "Gecersiz secim. Lutfen tekrar secin:";
        cin >> choice;
        choice = toupper(choice);
    }
    move = string(1,choice);// Convert char to string
   };
   //ComputerPlayer class
   class ComputerPlayer: public Player{
   public:
     ComputerPlayer(string playerName): Player(playerName){}
     virtual void makeMove() = 0; 

   };
   // RandomComputerPlayer class
   class RandomComputerPlayer: public ComputerPlayer{
   public:
     RandomComputerPlayer(string playerName):
   ComputerPlayer(playerName){}
    void makeMove() override{
        //Randomly select a move
        char choices[] = {'T','K','M'};
        move = string(1, choices[rand() %3]); // Randomly pick one of T,K, or M
        cout << name <<"hamlesi:" << move << endl;
    }
   };
   // Function to determine the winner of the round
   string determineWinner(string playerMove,string computerMove){
    if (playerMove == computerMove){
        return "draw";
    } else if ((playerMove == "T" && computerMove == "M")||
               (playerMove == "K" && computerMove == "T")||
               (playerMove == "M" && computerMove == "K")){
        return "win";
               } else {
                return "lose";
               }
   
   }
   // Game loop function
   void playGame(){
    srand(time(0)); // Seed for random number generation
    string playerName, computerName;
    cout << "Oyuncu adi:";
    cin >> playerName;
    cout << "Bilgisayar adi:";
    cin >> computerName;

    HumanPlayer player(playerName);
    RandomComputerPlayer computer(computerName);

    vector<string> history; // To keep track of past moves
    while(true){
        cout << "\n Yeni Tur Basliyor!" << endl;
        player.makeMove();
        computer.makeMove();
        cout << player. getName() <<"hamlesi:"<< player. getMove() << endl;
        cout << computer.getName() << "hamlesi:" <<computer.getMove() << endl;

        string result = determineWinner(player.getMove(), computer.getMove());
        if (result == "win"){
            cout << player.getName() << "kazandi!" << endl;
            player.updateScore("win");
        } else if (result == "lose"){
            cout << computer.getName() << "kazandi!" << endl;
        }else {
            cout << "Beraberlik!" << endl;
        }
        cout << player.getName() << "Puani:" << player.getScore() << endl;
        cout << computer.getName() << "Puani:" << computer.getScore() << endl;

        history.push_back(player.getMove() + "vs" + computer.getMove());
        cout << "Devam etmek ister misiniz? (E/H):";
        char playAgain;
        cin >> playAgain;

        if(toupper(playAgain)!= 'E'){
            cout << "\nOyunun Sonuclari:" << endl;
            cout << player.getName() <<"Toplam Puan:" << player.getScore() << endl;
            cout << computer.getName() << "Toplam Puan:" << computer.getScore() << endl;
            break;
        }
    }
   }
// Main function
int main(){
    playGame();
    return 0;
}

  