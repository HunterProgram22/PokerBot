function Tournament(players, type, buyin, speed) {
  this.players = players;
  this.type = type;
  this.buyin = buyin;
  this.speed = speed;

  this.getInfo = function(){
    return 'There are ' + this.players + ' players in a ' + this.buyin + ' buy-in ' + this.type +
      ' tournament that is a ' + this.speed + ' speed.'
  };

  this.position_dictionary = function() {
    if (this.players == 9) {
      dict = {
        1: "Small Blind",
        2: "Early Position",
        3: "Early Position",
        4: "Middle Position",
        5: "Middle Position",
        6: "Middle Position",
        7: "Late Position",
        8: "Late Position",
        9: "Button",
        };
      } else if (this.players == 6) {
        dict = {
            1: "Small Blind",
            2: "Early Position",
            3: "Middle Position",
            4: "Middle Position",
            5: "Late Position",
            6: "Button",
          };
      } return dict;
    }

}


var Tourn = new Tournament(6, "Double-up", 10.00, "Turbo");


// window.alert(Tourn.getInfo());
// window.alert(Tourn.position_dictionary()[6]);
