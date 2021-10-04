<script>
  export let answer = "Yes";
</script>

<div class="ball">
  <div class="hole">
    <div class="triangle">
      <p class="text">
        {answer}
      </p>
    </div>
  </div>
</div>

<style>
  .ball {
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .hole {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background-color: white;
  }

  .triangle {
    width: 0;
    height: 0;
    border-left: 100px solid transparent;
    border-right: 100px solid transparent;
    border-bottom: 150px solid blue;
    display: flex;
    justify-content: center;
  }
  .text {
    color: white;
    font-size: 50px;
    font-weight: bold;
    text-align: center;
  }
</style>
