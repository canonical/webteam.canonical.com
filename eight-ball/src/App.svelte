<script>
  import { Router, Link, Route } from "svelte-routing";
  import Ask from "./Ask.svelte";
  import Create from "./Create.svelte";

  export let url = "";
</script>

<Router {url}>
  <nav>
    <Link to="/">Home</Link>
    <Link to="/create">Create</Link>
  </nav>
  <div>
    <Route path="" component={Ask} />
    <Route path="create" component={Create} />
  </div>
</Router>
