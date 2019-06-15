var pokemon_list = document.getElementsByClassName("pokemon-list");
var Pokemon_Row_Test = '[data-pokemon-row="test"]';

var pokemon_row_test = document.querySelector(Pokemon_Row_Test);
pokemon_row_test.style.display="none";

function createPokemonRow(pokemonData) {
	var newLine = document.createElement("li");
	newLine.setAttribute("class","pokemon-row");
	var pokemonClickRow = document.createElement("a");
	pokemonClickRow.setAttribute("class","pokemon-click-row");

	var pokemonRowData = document.createElement("div");
	pokemonRowData.setAttribute("class","pokemon-row-data");

	var pokemonNameImage = document.createElement("span");
	pokemonNameImage.setAttribute("class","pokemon-name-image");
	var pokemonImage = document.createElement("img");
	pokemonImage.setAttribute("class","pokemon-image");
	pokemonImage.setAttribute("src",pokemonData.racePhoto);
	
	var pokemonName = document.createElement("span");
	pokemonName.setAttribute("class","pokemon-name");
	pokemonName.innerHTML = pokemonData.raceName;
	pokemonNameImage.appendChild(pokemonImage);
	pokemonNameImage.appendChild(pokemonName);
	var pokemonType = document.createElement("span");

	pokemonType.setAttribute("class","pokemon-type");
	pokemonType.innerHTML = pokemonData.raceType;

	var pokemonAbility = document.createElement("span");
	pokemonAbility.setAttribute("class","pokemon-ability");
	pokemonAbility.innerHTML = pokemonData.raceability;

	

	var pokemonAttributeValue = document.createElement("span");
	pokemonAttributeValue.setAttribute("class","pokemon-attribute-value");

	var pokemonHP = document.createElement("span");
	var pokemonATK = document.createElement("span");
	var pokemonDEF = document.createElement("span");
	var pokemonSPA = document.createElement("span");
	var pokemonSPD = document.createElement("span");
	var pokemonSPE = document.createElement("span");

	pokemonHP.setAttribute("class","pokemon-HP");
	pokemonATK.setAttribute("class","pokemon-ATK");
	pokemonDEF.setAttribute("class","pokemon-DEF");
	pokemonSPA.setAttribute("class","pokemon-SPA");
	pokemonSPD.setAttribute("class","pokemon-SPD");
	pokemonSPE.setAttribute("class","pokemon-SPE");

	pokemonHP.innerHTML = pokemonData.raceHp;
	pokemonATK.innerHTML = pokemonData.raceAtk;
	pokemonDEF.innerHTML = pokemonData.raceDef;
	pokemonSPA.innerHTML = pokemonData.raceSpa;
	pokemonSPD.innerHTML = pokemonData.raceSpd;
	pokemonSPE.innerHTML = pokemonData.raceSpe;

	pokemonAttributeValue.appendChild(pokemonHP);
	pokemonAttributeValue.appendChild(pokemonATK);
	pokemonAttributeValue.appendChild(pokemonDEF);
	pokemonAttributeValue.appendChild(pokemonSPA);
	pokemonAttributeValue.appendChild(pokemonSPD);
	pokemonAttributeValue.appendChild(pokemonSPE);

	pokemonRowData.appendChild(pokemonNameImage);
	pokemonRowData.appendChild(pokemonType);
	pokemonRowData.appendChild(pokemonAbility);
	pokemonRowData.appendChild(pokemonAttributeValue);

	pokemonClickRow.appendChild(pokemonRowData);
	

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