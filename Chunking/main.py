
def chunk_text(text):  
    
    if len(text) == 0:
        return []
      
    # Sentences Building 
    delimiters = [".", "?", "!"]
    sentences = []
    start = 0
    
    for i in range(len(text)):
        if text[i] in delimiters:
            sentences.append(text[start: i+1])
            start = i+1
        elif i == len(text)-1:
            sentences.append(text[start: i+1])
    
    if not sentences:
        return []
    
    # Chunking Logic 
    chunk_limit = 300
    chunks_list = []
    
    current_chunk = sentences[0]
    current_chunk_len = len(current_chunk.split())
    
    for i in range(1, len(sentences)):
        sentence = sentences[i]
        sentence_len = len(sentence.split())
        
        if current_chunk_len + sentence_len > chunk_limit:
            chunks_list.append(current_chunk)
            current_chunk = sentence
            current_chunk_len = sentence_len
        else:
            current_chunk += " " + sentence
            current_chunk_len += sentence_len
            
    chunks_list.append(current_chunk)
            
            
    return chunks_list

    
text = """The abyssopelagic zone, or the "abyss," remains one of the final frontiers of human discovery. This vast, silent realm begins at four thousand meters below the ocean surface, where sunlight is a forgotten memory and the pressure is equivalent to an elephant standing on a postage stamp. To understand the abyss is to understand the resilience of biological life under extreme duress. While the terrestrial world is governed by the rhythm of the sun, the deep ocean operates on a geological clock, fueled by the slow drift of marine snow—organic detritus falling from the productive upper layers of the sea.
In the late twentieth century, the discovery of hydrothermal vents revolutionized our understanding of biology. These underwater geysers, spewing mineral-rich water heated by the Earth’s magma, support entire ecosystems independent of photosynthesis. Instead, specialized bacteria utilize chemosynthesis, converting chemical energy from hydrogen sulfide into organic matter. This process supports giant tube worms, eyeless shrimp, and ghostly white crabs. The existence of these life forms suggests that life could potentially thrive on icy moons like Europa or Enceladus, where subsurface oceans are kept liquid by tidal heating.
# Exploration of these depths requires sophisticated engineering. Remotely Operated Vehicles (ROVs) and Autonomous Underwater Vehicles (AUVs) are equipped with titanium hulls and specialized lighting systems to withstand the crushing weight of the water column. Scientists navigating these crafts often describe the experience as "flying through a starless void." Every frame of video captured by an ROV might contain a species never before seen by human eyes. From the bioluminescent lures of the anglerfish to the delicate, gelatinous structures of deep-sea siphonophores, the aesthetic of the abyss is one of alien beauty and terrifying efficiency.
# However, the deep sea is no longer isolated from human impact. Recent expeditions have discovered microplastics and discarded fishing gear in the deepest trenches of the Pacific. The extraction of polymetallic nodules—potato-sized rocks rich in cobalt and nickel—poses a new threat to these fragile habitats. As the global demand for electric vehicle batteries grows, the pressure to mine the seabed increases. Balancing technological progress with environmental preservation is the defining challenge for the next generation of oceanographers. We are currently in a race to map the seafloor before we inadvertently destroy the very ecosystems we are trying to study. The silence of the abyss is being broken by the hum of sonar and the clatter of drill bits, signaling a new era of industrial interest in the dark."""

print(chunk_text(text))
