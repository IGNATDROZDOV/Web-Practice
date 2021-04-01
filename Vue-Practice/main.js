const App = {
	data() {
		return {
			app_title: 'ToDo',
			placeholder_head: 'Input your task name',
			input_value: '',
			list_of_tasks:['sdfsdf', 'sdfdsfds']
		}
	},

	methods: {
		input_change(event) {
			this.input_value = event.target.value
		},

		add_elem() {
			if (this.input_value !== ""){
				this.list_of_tasks.push(this.input_value)
				this.input_value = ''
			}
		},

		delete_elem(ind){
			this.list_of_tasks.splice(ind, 1)
		},

		toUpperCase(task){
			return task.toUpperCase()
		}
	}
}

Vue.createApp(App).mount('#app')