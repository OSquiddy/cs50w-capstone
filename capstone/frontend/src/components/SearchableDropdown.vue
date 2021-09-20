<template>
  <div class="dropdown">
    <input type="text" :placeholder="placeholder" :id="id" :name="id" @keyup="filterFunction()" @focus="toggleDropdown()" v-model="user.fullname" autocomplete="off">
    <ul id="myDropdown" class="dropdown-content" :class="open && 'show'">
      <li v-if="isPatient">
        <div class="dropdown-row-container">
          <div class="img add-patient-img-container">
            <img src="../assets/add-patient.svg" alt="add-patient-icon" class="add-patient-img">
          </div>
          <router-link :to="{ name: 'add-patient' }">
            <div class="add-patient"> Add new patient </div>
          </router-link>
        </div>
      </li>
      <li v-for="user in dataList" :key="user.id" @click="isPatient ? selectPatient(user.id) : selectDoctor(user.id)">
        <div class="dropdown-row-container">
          <div class="img"></div>
          <div class="dropdown-content-text user-group">
            <div class="user-name"> {{user.fullname}} </div>
            <div class="user-id"> ID: {{user.id}} </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: 'SearchableDropdown',
  props: ['placeholder', 'dataList', 'isPatient', 'id'],
  data() {
    return {
      open: false
    }
  },
  computed: {
    ...mapState(['patient', 'doctor']),
    user () {
      return this.isPatient ? this.patient : this.doctor
    }
  },
  created () {
    window.onclick = (event) => {
      if (event.target.id !== this.id && this.open) {
        this.toggleDropdown()
      }
    }
  },
  beforeDestroy () {
    window.removeEventListener('click', (event) => {
      if (event.target.id !== this.is && this.open) {
        this.toggleDropdown()
      }
    })
  },
  mounted () {
  },
  methods: {
    ...mapActions(['getPatientInfo', 'getDoctorInfo']),
    toggleDropdown () {
      this.open = !this.open
    },
    filterFunction () {
      const input = document.getElementById(this.id)
      const filter = input.value.toUpperCase()
      const div = document.getElementById('myDropdown')
      const li = div.getElementsByTagName('li')
      for (let i = 0; i < li.length; i++) {
        const txtValue = li[i].textContent || li[i].innerText
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = ''
        } else {
          li[i].style.display = 'none'
        }
      }
    },
    selectPatient (id) {
      this.getPatientInfo(id)
      this.open = !this.open
    },
    selectDoctor (id) {
      this.getDoctorInfo(id)
      this.open = !this.open
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
:where(#doctor, #patient):focus {outline: 3px solid #ddd;}

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
  list-style: none;
  padding: 0;
  margin: 0;
}

/* Links inside the dropdown */
.dropdown-content li {
  color: black;
  padding: 5px 16px;
  text-decoration: none;
  display: block;
  &:first-child {
    padding-top: 15px;
  }
  &:hover {
    background-color: #f1f1f1;
    cursor: pointer;
  }
}

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
