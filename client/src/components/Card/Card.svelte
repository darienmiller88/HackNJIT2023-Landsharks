<script lang="ts">
    export let title: string 
    export let value: any
</script>

<div class="card">
    <div class="title">{title}</div>
    <div class="value">{value}</div>
</div>

<style lang="scss">
    .card{
        width: fit-content;
        padding: 40px 40px;
        border-radius: 5px;
        transition: 0.3s;

        border: 2px solid var(--primary);
        color: var(--primary);

        &:hover{
            background-color: var(--primary-transparent);
            color: antiquewhite;
        }
    }
</style>