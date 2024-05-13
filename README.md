# celltype-prediction-benchmark
### Overview
This repository is dedicated to evaluating the performance of OmnibusX and Azimuth, a reference-based cell type prediction tool, across a diverse set of single-cell RNA sequencing (scRNA-seq) datasets. The analysis spans 22 datasets from 11 different tissues. For comprehensive benchmarking, subsets of these datasets, along with the authors' standardized annotations and both raw and standardized prediction results from Azimuth and OmnibusX, have been made available on Zenodo: https://doi.org/10.5281/zenodo.11183242.

### Performance evaluation metrics
The performance of the OmnibusX and Azimuth prediction tools is evaluated across three main dimensions:

#### I. Score by studies

<ul>
  <li><b>OmnibusX performance</b>: Consistent across various tissues and studies, demonstrating robust adaptability and accuracy.</li>
  <li><b>Azimuth performance</b>: Generally performs poorly on datasets not included in its reference set, indicating limited adaptability to external datasets.</li>
  <li><b>Comparison</b>: OmnibusX consistently outperforms Azimuth across almost all datasets.</li>
</ul>

<p align="center">
 <img src="https://github.com/OmnibusXLab/celltype-prediction-benchmark/assets/169631565/d8b713d2-7c5f-4d02-b238-d262d0c9b37f" style="width: 100%" />
</p>

<b> Table 1: Cohen&#39;s Kappa scores by studies</b>
<table style="width: 100%">
    <tr>
        <td rowspan="2" align="center">Source</td>
        <td rowspan="2" align="left">Tissue</td>
        <td colspan="2" align="center">Cohen&#39;s Kappa score</td>
        <td rowspan="2" align="left">Download link</td>
    </tr>
    <tr>
        <td align="center">Azimuth</td>
        <td align="center">OmnibusX</td>
    </tr>
    <tr>
        <td rowspan="7">Azimuth&#39;s <br>reference</td>
        <td>brain</td>
        <td><b>0.9603139742</b></td>
        <td>0.9390266193</td>
        <td><a target="_blank" href="https://portal.brain-map.org/atlases-and-data/rnaseq/human-m1-10x">human_m1_10x</a></td>
    </tr>
    <tr>
        <td>pancreas</td>
        <td><b>0.9531699703</b></td>
        <td>0.9469605035</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/6e8c5415-302c-492a-a5f9-f29c57ff18fb">GSE85241</a></td>
    </tr>
    <tr>
        <td>heart</td>
        <td>0.8684306121</td>
        <td><b>0.965068149</b></td>
        <td><a target="_blank" href="https://www.heartcellatlas.org/">ERP123138</a></td>
    </tr>
    <tr>
        <td>liver</td>
        <td>0.8281289277</td>
        <td><b>0.9241128587</b></td>
        <td><a target="_blank" href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115469">GSE115469</a></td>
    </tr>
    <tr>
        <td>kidney</td>
        <td>0.7352549721</td>
        <td><b>0.8444745325</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/bcb61471-2a44-4d00-a0af-ff085512674c">GSE183276</a></td>
    </tr>
    <tr>
        <td>lung</td>
        <td>0.6968786073</td>
        <td><b>0.8787800563</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/5d445965-6f1a-4b68-ba3a-b8f765155d3a">syn21041850</a></td>
    </tr>
    <tr>
        <td>bone marrow</td>
        <td>0.6807361481</td>
        <td><b>0.8806892622</b></td>
        <td><a target="_blank" href="https://explore.data.humancellatlas.org/projects/cc95ff89-2e68-4a08-a234-480eca21ce79">ERP122984</a></td>
    </tr>
    <tr>
        <td rowspan="15">External <br> data</td>
        <td>bone marrow</td>
        <td>0.8008471978</td>
        <td><b>0.8679295956</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/26b5b4f6-828c-4791-b4a3-abb19e3b1952">GSE216005</a></td>
    </tr>
    <tr>
        <td>brain</td>
        <td>0.664736442</td>
        <td><b>0.9135566933</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/9d63fcf1-5ca0-4006-8d8f-872f3327dbe9">seeker_et_al</a></td>
    </tr>
    <tr>
        <td>heart</td>
        <td>0.7970372168</td>
        <td><b>0.8552565266</b></td>
        <td><a target="_blank" href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE165838">GSE216019</a></td>
    </tr>
    <tr>
        <td>kidney</td>
        <td>0.7711450523</td>
        <td><b>0.824633467</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/b3e2c6e3-9b05-4da9-8f42-da38a664b45b">GSE131882</a></td>
    </tr>
    <tr>
        <td>liver</td>
        <td>0.354816257</td>
        <td><b>0.8592514844</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/74e10dc4-cbb2-4605-a189-8a1cd8e44d8c">GSE192740</a></td>
    </tr>
    <tr>
        <td>lung</td>
        <td>0.7197451536</td>
        <td><b>0.879019929</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/625f6bf4-2f33-4942-962e-35243d284837">GSE161382</a></td>
    </tr>
    <tr>
        <td>pancreas</td>
        <td><b>0.8641038128</b></td>
        <td>0.8261070836</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/51544e44-293b-4c2b-8c26-560678423380">GSE148073</a></td>
    </tr>
    <tr>
        <td>pbmc</td>
        <td>0.717368913</td>
        <td><b>0.8444486116</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/ecb739c5-fe0d-4b48-81c6-217c4d64eec4">GSE247917</a></td>
    </tr>
    <tr>
        <td>pbmc</td>
        <td>0.5904696495</td>
        <td><b>0.8151155515</b></td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/03f821b4-87be-4ff4-b65a-b5fc00061da7">EGAD00001007718</a></td>
    </tr>
    <tr>
        <td>breast</td>
        <td>-</td>
        <td>0.9386349816</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/48259aa8-f168-4bf5-b797-af8e88da6637">E-MTAB-13664</a></td>
    </tr>
    <tr>
        <td>breast</td>
        <td>-</td>
        <td>0.8369720101</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/4195ab4c-20bd-4cd3-8b3d-65601277e731">GSE195665</a></td>
    </tr>
    <tr>
        <td>colon</td>
        <td>-</td>
        <td>0.9119828979</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/2b02dff7-e427-4cdc-96fb-c0f354c099aa">GSE134809</a></td>
    </tr>
    <tr>
        <td>colon</td>
        <td>-</td>
        <td>0.8140441488</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/17481d16-ee44-49e5-bcf0-28c0780d8c4a">E-MTAB-8901</a></td>
    </tr>
    <tr>
        <td>eye</td>
        <td>-</td>
        <td>0.9907107326</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/939769a8-d8d2-4d01-abfc-55699893fd49">GSE135133</a></td>
    </tr>
    <tr>
        <td>eye</td>
        <td>-</td>
        <td>0.863679996</td>
        <td><a target="_blank" href="https://cellxgene.cziscience.com/collections/e9c73b68-e980-49c2-8d0d-1c9cab21507e">GSE169047</a></td>
    </tr>
</table>

#### II. Score by cell types
<ul>
  <li><b>Azimuth</b>: Shows a significant performance drop, particularly with immune cell subtypes such as B cells and T/NK cells, which are typically more challenging due to their close genetic profiles.</li>
  <li><b>OmnibusX</b>: Maintains stable performance across these challenging cell subtypes, underscoring its superior prediction accuracy and robustness.</li>
</ul>

<b> Table 2: Cohen&#39;s Kappa scores by cell types</b>
<table>
    <tr>
        <td align="center">F1-score</td>
        <td align="center">B cell</td>
        <td align="center">T/NK cells</td>
        <td align="center">endothelial cell</td>
        <td align="center">myeloid leukocyte</td>
        <td align="center">stromal cell</td>
        <td align="center">neuron</td>
        <td align="center">epithelial</td>
        <td align="center">glial cell</td>
    </tr>
    <tr>
        <td>Azimuth</td>
        <td>0.5989131</td>
        <td>0.60018248</td>
        <td>0.73388801</td>
        <td>0.81469631</td>
        <td>0.81798307</td>
        <td>0.82249145</td>
        <td>0.83814041</td>
        <td>0.98230289</td>
    </tr>
    <tr>
        <td>OmnibusX</td>
        <td><b>0.92183027</b></td>
        <td><b>0.85117904</b></td>
        <td><b>0.84456937</b></td>
        <td><b>0.90978901</b></td>
        <td><b>0.87832225</b></td>
        <td><b>0.9505289</b></td>
        <td><b>0.8923383</b></td>
        <td><b>0.98339951</b></td>
    </tr>
</table>

#### III. Cluster dispersion influence
As the degree of cluster dispersion increases, the performance of each tool is affected differently:
<ul>
  <li><b>OmnibusX</b>: Exhibits a slight decline in performance, maintaining a relatively high level of accuracy despite increased dispersion.</li>
  <li><b>Azimuth</b>: Performance drops exponentially with increased dispersion, highlighting significant limitations in handling dispersed clusters.</li>
</ul>

<p align="center">
  <img src="https://github.com/OmnibusXLab/celltype-prediction-benchmark/assets/169631565/e6f0101d-1974-4aff-a5ea-650f7dbcec67" style="width: 100%" />
</p>

### Citation
If you use the data or methodology from this repository in your research, please cite the corresponding Zenodo deposit and this repository appropriately.
