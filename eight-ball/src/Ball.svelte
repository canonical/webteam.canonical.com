<script>
  export let answer;
</script>

<div class="ball {answer ? 'shake' : ''} ">
  <div class="hole">
    {#if !!answer}
      <div class="triangle">
        <p class="text">
          {answer}
        </p>
      </div>
    {/if}
  </div>
</div>
<div class="shadow" />

<style>
  .ball {
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(circle at 30% 30%, #333, #000);
  }

  .shadow {
    margin-left: 0;
    margin-top: -20px;
    width: 600px;
    height: 50px;
    background: radial-gradient(#000f, #fff0 72%);
    border-radius: 50%;
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

  @keyframes shake {
    0% {
      transform: rotate(1deg) translate(3px, 4px);
    }
    5% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    10% {
      transform: rotate(0deg) translate(0px, -5px);
    }
    15% {
      transform: rotate(2deg) translate(4px, 0px);
    }
    20% {
      transform: rotate(1deg) translate(-3px, 3px);
    }
    25% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    30% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    35% {
      transform: rotate(-2deg) translate(3px, 4px);
    }
    40% {
      transform: rotate(0deg) translate(-3px, -3px);
    }
    45% {
      transform: rotate(-1deg) translate(4px, 4px);
    }
    50% {
      transform: rotate(1deg) translate(-4px, 3px);
    }
    55% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    60% {
      transform: rotate(0deg) translate(0px, -5px);
    }
    65% {
      transform: rotate(2deg) translate(4px, 0px);
    }
    70% {
      transform: rotate(1deg) translate(-3px, 3px);
    }
    75% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    80% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    85% {
      transform: rotate(1deg) translate(1px, -2px);
    }
    100% {
      transform: rotate(0deg) translate(0px, 0px);
    }
  }
  .shake {
    animation: shake 1.2s ease-out 2;
  }
</style>
