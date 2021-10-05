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
  @font-face {
    font-display: optional;
    font-family: "Ubuntu";
    font-style: normal;
    font-weight: 300;
    src: url("https://assets.ubuntu.com/v1/e8c07df6-Ubuntu-L_W.woff2")
        format("woff2"),
      url("https://assets.ubuntu.com/v1/8619add2-Ubuntu-L_W.woff")
        format("woff");
  }
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

  :global(body) {
    margin: 0;
    padding: 0;
    font-family: "Ubuntu", sans-serif;
    font-size: 16px;
    color: #fff;
    height: 100vh;
    overflow: hidden;
  }
</style>
