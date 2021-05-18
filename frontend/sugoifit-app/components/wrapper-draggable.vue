<script>
import draggable from 'vuedraggable'
const vuedraggableProps = {
    options: Object,
    // list: { type: Array, required: false, default: null }, We wouldn't really need this,
    // value: { type: Array, required: false, default: null }, also this.
    noTransitionOnDrag: { type: Boolean, default: false },
    clone: { type: Function, default: original => (original) },
    element: { type: String, default: 'div' },
    tag: { type: String, default: null },
    move: { type: Function, default: null },
    componentData: { type: Object, required: false, default: null }
}
export default {
    props: vuedraggableProps,
    components: { draggable },
    data: () => ({
        list: [] // You can name this whatever you want
    }),
    mounted () {
        // You can change this `key` variable to whatever you want, 
        // but it must be unique.
        let key = 0 
        const filtered = this.$slots.default.filter(
          vnode => vnode.tag !== undefined
        )
        this.list = filtered.map(vnode => ({ id: key++, vnode }))
    },
    methods: {
        getProps () {
            // Remember to add these to `props` property.
            const { options, noTransitionOnDrag, clone, element, tag, move, componentData } = this
            return { options, noTransitionOnDrag, clone, element, tag, move, componentData }
        }
    },
    render (h) {
        return h('draggable', { 
            props: { ...this.getProps(), value: this.list },
            attrs: { ...this.$attrs },
            on: { input: ($event) => { this.list = $event } }
        }, this.list.map(el => {
           el.vnode.key = el.id
           return el.vnode
        }))
    }
}
</script>