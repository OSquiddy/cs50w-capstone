<template>
  <div class="search-container">
      <div class="container-fluid">
        <div class="row">
          <div class="col">
            <div class="search-header">{{searchHeader}}</div>
            <form action="/" method="post">
              <div class="search-bar mt-2 mb-3">
                <img src="../assets/search.svg" alt="">
                <input type="text" name="search" id="search" placeholder="Search">
              </div>
              <div class="date-picker mb-2">
                <div class="month-group">
                  <span>April</span>
                  <img src="../assets/dropdown-arrow.svg" alt="dropdown-arrow">
                </div>
                <div class="year-group">
                  <span>2021</span>
                  <img src="../assets/dropdown-arrow.svg" alt="dropdown-arrow">
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'SearchContainer',
  data() {
    return { }
  },
  props: {
    searchHeader: {
      type: String
    }
  }
}
</script>

<style lang="scss" scoped>
.search-bar {
  border: 1px solid #d2d2d2;
  background-color: #f5f5f5;
  border-radius: 3px;
  padding: 2px 14px;
  #search {
  outline: none;
  border: none;
  display: inline-flex;
  margin-left: 10px;
  width: 90%;
  color: #828282; //Search color
  background: transparent;
  }
}

.search-container {
  // z-index: 3;
  // box-shadow: 0 1px 3px 0px rgba(0,0,0,0.25);
  .search-header {
    margin-bottom: 12px;
  }
}

.date-picker {
  display: flex;
  .month-group {
    display: inline-block;
    margin-left: auto;
    span {
      margin-right: 5px;
    }
    margin-right: 20px;
  }

  .year-group {
    display: inline-block;
    span {
      margin-right: 5px;
    }
  }
}
</style>
