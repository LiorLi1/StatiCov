/*const data = [
  [null, null, null, null, null, "HI"],
  [null, null, null, null, null, "HAR"],
  [null, null, null, null, null, "MASOR"],
  [null, null, null, null, null, "ARA"],
  [null, null, null, null, null, "NOTS"],
  [null, null, null, null, null, "BLI"],
]

RELIGION_INDEX = 5

const countReligion = {
  "HI": 0,
  "HAR": 0,
  "MASOR": 0,
  "ARA": 0,
  "NOTS": 0,
  "BLI": 0,
}

function handleData_2(data){
  const labels = Object.values(countReligion);
  const datasets = Object.keys()

  for(const item of data) {
    countReligion[item[RELIGION_INDEX]] += 1;
  }
  console.log(countReligion)
  return {
    data: Object.values(countReligion),
    label: entryKey,
    borderColor: COLORS[index % COLORS.length],
    fill: false
  }
}*/
new Chart(document.getElementById("doughnut-chart"), {
  type: 'doughnut',
  data: {
    labels,
    datasets
  },
  options: {
    title: {
      display: true,
      text: 'נתוני נדבקים 2020 - ע"פ דת'
    }
  }
});

/*function handleError(error){
  console.log({error});
}

$.ajax({url:"http://localhost:8000/Staticov/datapatient", success: handleData_2, error: handleError});*/