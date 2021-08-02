<template>
  <div class="dropdown">
    <input type="text" :placeholder="placeholder" id="myInput" @keyup="filterFunction()" @blur="hide()" @focus="show()">
    <div id="myDropdown" class="dropdown-content">
      <a href="#about">
        <div class="dropdown-row-container">
          <div class="img add-patient-img-container">
            <img src="../assets/add-patient.svg" alt="add-patient-icon" class="add-patient-img">
          </div>
          <div class="add-patient"> Add new patient </div>
        </div>
      </a>
      <a href="#" v-for="patient in patients" :key="patient.id">
        <div class="dropdown-row-container">
          <div class="img"></div>
          <div class="dropdown-content-text patient-group">
            <div class="patient-name"> {{patient.first_name}} {{patient.last_name}} </div>
            <div class="patient-id"> ID: {{patient.id}} </div>
          </div>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchableDropdown',
  props: ['placeholder'],
  data() {
    return {
      patients: [
        { id: 12, first_name: 'Harry', last_name: 'Potter' },
        { id: 14, first_name: 'Hermione', last_name: 'Granger' },
        { id: 13, first_name: 'Ron', last_name: 'Weasley' }
      ]
    }
  },
  methods: {
    hide () {
      document.getElementById('myDropdown').classList.remove('show')
    },
    show () {
      document.getElementById('myDropdown').classList.add('show')
    },
    filterFunction () {
      const input = document.getElementById('myInput')
      const filter = input.value.toUpperCase()
      const div = document.getElementById('myDropdown')
      const a = div.getElementsByTagName('a')
      for (let i = 0; i < a.length; i++) {
        const txtValue = a[i].textContent || a[i].innerText
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          a[i].style.display = ''
        } else {
          a[i].style.display = 'none'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
/* Dropdown Button */
.dropbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

/* Dropdown button on hover & focus */
.dropbtn:hover, .dropbtn:focus {
  background-color: #3e8e41;
}

/* The search field */
#myInput {
  box-sizing: border-box;
  background-image: url('../assets/search.svg');
  background-position: 14px 12px;
  background-repeat: no-repeat;
  font-size: 16px;
  padding: 14px 20px 12px 45px;
  border: none;
  border-bottom: 1px solid #ddd;
}

/* The search field when it gets focus/clicked on */
#myInput:focus {outline: 3px solid #ddd;}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f6f6f6;
  min-width: 230px;
  border: 1px solid #ddd;
  z-index: 1;
  max-height: 300px;
  overflow: auto;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 5px 16px;
  text-decoration: none;
  display: block;
  &:first-child {
    padding-top: 15px;
  }
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #f1f1f1}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {display:block;}

.dropdown-row-container {
  display: flex;
}

.img {
  background: var(--medium-gray);
  width: 30px;
  aspect-ratio: 1;
  display: flex;
  align-self: center;
  border-radius: 50%;
  margin-right: 20px;
}

.add-patient-img-container {
  background: transparent;
  .add-patient-img {
    width: 60%;
    margin: 0 auto;
  }
}
</style>
