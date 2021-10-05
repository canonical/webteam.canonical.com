<script>
  import { Router, Link, Route } from "svelte-routing";
  import Ask from "./Ask.svelte";
  import Create from "./Create.svelte";

  export let url = "";
</script>

<Router {url}>
  <div class="background">
    <Route path="" component={Ask} />
    <Route path="create" component={Create} />
  </div>
</Router>

<style>
  .background {
    background-color: #030364;
    opacity: 1;
    height: 100vh;
    background-image: repeating-radial-gradient(
        circle at 0 0,
        transparent 0,
        #030364 40px
      ),
      repeating-linear-gradient(#7500cd55, #7500cd);
  }

  .shelf {
    position: fixed;
    bottom: 0;
    width: 100vw;
    height: 10vh;
    background: linear-gradient(#921212, rgb(84 0 0));
  }

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: "Roboto", sans-serif;
    font-size: 16px;
    color: #fff;
    height: 100vh;
    overflow: hidden;
  }
</style>
