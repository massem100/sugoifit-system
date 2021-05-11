<template>
  <div>
    <b-table-simple responsive="">
      <b-thead>
        <b-tr>
          <b-th>User Name</b-th>
          <b-th>Role</b-th>
          <b-th>Actions</b-th>
        </b-tr>
      </b-thead>
      <b-tbody>
        <b-tr v-for="(user,idx) in users" :key="idx">
          <b-td>{{user.name}}</b-td>
          <b-td>{{user.role}}</b-td>
          <b-td>
            <b-button size="sm" variant="info">edit</b-button>
            <b-button size="sm" variant="danger">delete</b-button>
          </b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
  </div>
</template>

<script>
    export default {
        name: "user-management",
        data() {
            return {
                users: [
                    {name: 'Monique', role: 'Business Owner', id: 1},
                    {name: 'Bethany', role: 'Employee', id: 2},
                    {name: 'John', role: 'Financial Manager', id: 3},
                ]
            }
        }
    }
</script>

<style scoped>

</style>
