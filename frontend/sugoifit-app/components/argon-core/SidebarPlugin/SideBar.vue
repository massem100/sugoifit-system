<template>
  <div class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light bg-white">
    <div class="scrollbar-inner" ref="sidebarScrollArea">
      <div class="sidenav-header d-flex justify-content-center">
        <a class="m-4" href="#">
              <!-- <img :src="logo" class="navbar-brand-img" alt="Sidebar logo" /> -->
              <i class="ni ni-lg ni-sound-wave"></i>
              <span >  SugoiFit <span class = "font-weight-bold"> Dashboard</span></span>
             
            </a>
      </div>
      <slot></slot>
      <div class="navbar-inner">
        <ul class="navbar-nav">
          <slot name="links">
            <sidebar-item
              v-for="(link, index) in sidebarLinks"
              :key="link.name + index"
              :link="link"
            >
              <sidebar-item
                v-for="(subLink, index) in link.children"
                :key="subLink.name + index"
                :link="subLink"
              >
              </sidebar-item>
            </sidebar-item>
          </slot>
        </ul>
        <slot name="links-after"></slot>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "sidebar",
  props: {
    // title: {
    //   type: String,
    //   default: "Creative Tim",
    //   description: "Sidebar title",
    // },
    // shortTitle: {
    //   type: String,
    //   default: "CT",
    //   description: "Sidebar short title",
    // },
    logo: {
      type: String,
      default: "/img/brand/green.png",
      description: "Sidebar app logo",
    },
  
    sidebarLinks: {
      type: Array,
      default: () => [],
      description:
        "List of sidebar links as an array if you don't want to use components for these.",
    },
    autoClose: {
      type: Boolean,
      default: true,
      description:
        "Whether sidebar should autoclose on mobile when clicking an item",
    },
  },
  // provide() {
  //   return {
  //     autoClose: this.autoClose,
  //   };
  // },
  methods: {
   
  }

};
</script>
