var pokemon_list = document.getElementsByClassName("pokemon-list");
var Pokemon_Row_Test = '[data-pokemon-row="test"]';

var pokemon_row_test = document.querySelector(Pokemon_Row_Test);
pokemon_row_test.style.display="none";

function createPokemonRow(pokemonData) {
	var newLine = document.createElement("li");
	newLine.setAttribute("class","pokemon-row");
	var pokemonClickRow = document.createElement("a");
	pokemonClickRow.setAttribute("class","pokemon-click-row");
	var pokemonNameImage = document.createElement("span");
	pokemonNameImage.setAttribute("class","pokemon-name-image");
	var pokemonImage = document.createElement("img");
	pokemonImage.setAttribute("class","pokemon-image");
	pokemonImage.setAttribute("src",pokemonData.racePhoto);
	pokemonClickRow.appendChild(pokemonNameImage);
	pokemonNameImage.appendChild(pokemonImage);
	newLine.appendChild(pokemonClickRow);
	pokemon_list[0].appendChild(newLine);
}

function getMonsterData() {
	$.ajax({
			url:"/getMonsterData/",
			type:"GET",
			data:{
			},
			success:function(ret) {
				var returnData = JSON.parse(ret);
				var monsterList = returnData["monsterList"];
				monsterList.forEach(createPokemonRow);
			}
		})
}

getMonsterData();