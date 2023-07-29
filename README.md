# Logitistics-Blockchain

This program is a prototype which demonstrates a component in the optimization of logistics within the supply chain. The program revolves around a truck visiting six locations to deliver product shipments collected initially from a depot. At each shipment location, data is reported by the truck which is then utilized to mint an NFT. This NFT is processed through a Smart Contract utilizing the Goerli TestNet. In respect to this project, the "dataupload.py" file can be employed to upload data which is minted as an NFT and uploaded to the blockchain through the Verbwire API. Although this data is randomized for the sake of this prototype, it can easily be fitted to match realtime recieved data. Once all the NFTs in regard to that journey are minted, all of the Token IDs are returned for the user to be capable of later calling the data stored in the NFT. Using the "metadataread.py" program provided, data can be read from the NFTs corresponding to the Token IDs put in the "ids" list. The value of this project is that it demonstrates the utility of blockchain technology in the logistics industry. Blockchain provides a variety of benefits to the logistics industry which can revolutionize supply chain processes such as:
  
  - Increased transparency due to to the immutable and freely accessible ledger
  - Upgraded security due to the encryption of the data
  - Increased efficiency in the supply chain process due to the ease of data sharing and communication among parties involved within the supply chain
  - Decreased manual administrative requirements due to a digitized and automated data storage process which greatly reduces manual data entry necessary for logistics operations
  - Promoted collaboration due to a lack of a central authority
