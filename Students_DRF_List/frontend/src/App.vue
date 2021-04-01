<template>
  <div id="app">
    <form @submit.prevent="addStudents">
      <div class="form-group row">
        <input
          type="text"
          class="form-control col-2 mx-2"
          placeholder="Enter name"
          v-model="student.name"
        />
        <input
          type="text"
          class="form-control col-2 mx-2"
          placeholder="Enter surname"
          v-model="student.surname"
        />
        <input
          type="text"
          class="form-control col-2 mx-2"
          placeholder="Enter patronymic"
          v-model="student.patronymic"
        />
        <select class="selection_menu col-2 mx-2" v-model="student.department">
          <option value="" disabled selected>Select your faculty</option>
          <option v-for="department in departments" :key="department">
            {{ department }}
          </option>
        </select>
        <button class="btn btn-success">Add new student</button>
      </div>
    </form>

    <div
      class="elem_of_department"
      v-for="department in departments"
      :key="department"
    >
      <input
        type="checkbox"
        v-model="checkedDepartments"
        v-bind:value="department"
      />
      {{ department }}
    </div>

    <table class="table">
      <thead>
        <th class="table_header" colspan="5">List of students</th>
      </thead>
      <tbody v-if="students.length !== 0">
        <td class="len_header" colspan="5">
          Amount of students
          <h1 class="num_head">{{ filteredStudents.length }}</h1>
        </td>
        <tr v-for="student in filteredStudents" :key="student.id">
          <td>{{ student.name }}</td>
          <td>{{ student.surname }}</td>
          <td>{{ student.patronymic }}</td>
          <td>{{ student.department }}</td>
          <td>
            <button
              class="btn btn-outline-danger btn-sm mx-1"
              @click="deleteStudent(student)"
            >
              delete
            </button>
          </td>
        </tr>
      </tbody>
      <div class="alternative_header" v-else>There are no students</div>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      student: {
        name: "",
        surname: "",
        patronymic: "",
        department: "",
      },
      departments: ["electrotechnical", "automechanical", "building"],
      students: null,
      checkedDepartments: [],
    };
  },

  async created() {
    await this.getStudents();
  },

  methods: {
    async getStudents() {
      let response = await fetch("http://127.0.0.1:8000/student_app/students/");
      this.students = await response.json();
    },

    async deleteStudent(student) {
      this.getStudents();
      await fetch(`http://127.0.0.1:8000/student_app/students/${student.id}/`, {
        method: "delete",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(student),
      });
      await this.getStudents();
    },

    async addStudents() {
      this.getStudents();
      await fetch("http://127.0.0.1:8000/student_app/students/", {
        method: "Post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      this.student.name = "";
      this.student.surname = "";
      this.student.patronymic = "";
      this.student.department = "";
      await this.getStudents();
    },
  },

  computed: {
    filteredStudents() {
      if (!this.checkedDepartments.length) return this.students;
      return this.students.filter((student) =>
        this.checkedDepartments.includes(student.department)
      );
    },
  },
};
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  width: 100%;
}

.table_header {
  font-size: 3rem;
  font-weight: 300;
}

.form-group {
  margin: 5% 0 0 5%;
}

.alternative_header {
  font-size: 2rem;
}

.len_header {
  font-size: 2rem;
}

.num_head {
  font-size: 2rem;
  color: red;
}

.elem_of_department {
  font-size: 150%;
  display: inline-block;
  padding: 30px;
}
</style>

