<script>
  import { Map, TileLayer, CircleMarker, Popup, Polyline } from "sveaflet";
  import { onMount } from "svelte";
  import { Stretch } from "svelte-loading-spinners";

  import { lines } from "./assets/lines.json";

  onMount(() => {
    console.log(lines);
  });
</script>

<div class="w-screen h-screen">
  {#if lines.length == 0}
    <Stretch size="60" color="#FF3E00" unit="px" duration="1s" />
  {:else}
    <Map options={{ center: [28.663357, 77.185395], zoom: 13 }}>
      <TileLayer url={"https://tile.openstreetmap.org/{z}/{x}/{y}.png"} />

      {#each lines as line}
        {#each line.stations as station}
          <CircleMarker
            latLng={station.coordinates}
            options={{ radius: 16, color: line.hex_color }}
          >
            <Popup options={{ content: station.name }} />
          </CircleMarker>
        {/each}
        <Polyline
          latLngs={Array.from(line.stations, (station) => station.coordinates)}
          options={{ color: line.hex_color }}
        />
      {/each}
    </Map>
  {/if}
</div>
