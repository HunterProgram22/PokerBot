var PositionStrategy = {
  tier_one: ["AA", "KK", "QQ", "JJ", "AK"],
  tier_two: ["TT", "99", "88", "77", "AQ", "AJ"],
  tier_three: ["ATs", "KQs", "QJs", "JTs"],
  tier_four: ["66", "55", "44", "33", "22","A9s", "109s", "98s"],
}

function action(cards){
  if (PositionStrategy.tier_one.includes(cards)){
    window.alert("Bet");
  };
}

action("AA");
