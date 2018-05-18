var PositionStrategy = {
  tier_one: ["AA", "KK", "QQ", "JJ", "AK"],
  tier_two: ["TT", "99", "88", "77", "AQ", "AJ"],
  tier_three: ["ATs", "KQs", "QJs", "JTs"],
  tier_four: ["66", "55", "44", "33", "22","A9s", "109s", "98s"],
  };

var position_dictionary_nine = {
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

function printDecision(decision) {
  var placeholder = document.getElementById('Decision');
  placeholder.innerHTML = decision;
  }

function getAction(cards, position) {
  if (position_dictionary_nine[position.value] == "Small Blind"){
    if (PositionStrategy.tier_one.includes(cards.value)){
      return "Bet";
      } else {
        return "Fold";
      }
    } else {
      return "No position dict";
    }
  }

var button = document.getElementById('cardSubmit');

button.onclick = function(){
    var cards = document.getElementById("cards");
    var position = document.getElementById("position");
    var decision = getAction(cards, position);
    printDecision(decision);
  }
