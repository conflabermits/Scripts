package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

type Options struct {
	HostHeader string
	JsonFile   string
	Url        string
	Depth      string
}

type ShortOutput struct {
	Name       string `json:"name"`
	StatusCode string `json:"statusCode"`
}

func health_checker_http_req(url string, hostHeader string) string {
	client := &http.Client{
		Timeout: time.Second * 30,
	}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return err.Error()
	} else {
		// override Host header, if specified
		if len(hostHeader) > 0 {
			req.Host = hostHeader
		}
		req.Header.Set("user-agent", "health_checker-go")
		//req.Header.Add("X-Forwarded-Proto", "https")
		resp, err := client.Do(req)
		if err != nil {
			return err.Error()
		} else {
			body, err := ioutil.ReadAll(resp.Body)
			defer resp.Body.Close()
			if err != nil {
				return err.Error()
			} else {
				return string(body)
			}
		}
	}
}

func parse_json_file(input_file string) map[string]interface{} {

	//fmt.Println("\nHello parse_json_file!")
	jsonFile, err := os.Open(input_file)
	if err != nil {
		fmt.Println(err)
	} /* else {
		fmt.Println("Successfully opened json file")
	} */
	defer jsonFile.Close()
	//fmt.Println("\t", "jsonFile", reflect.TypeOf(jsonFile))

	byteValue, _ := ioutil.ReadAll(jsonFile)
	//fmt.Println("\t", "byteValue", reflect.TypeOf(byteValue))

	var result map[string]interface{}
	//fmt.Println("\t", "result", reflect.TypeOf(result))

	json.Unmarshal([]byte(byteValue), &result)
	//fmt.Println("\t", "&result", reflect.TypeOf(&result))

	return result

}

func example_json(jsonfile string) {

	//fmt.Println("\nHello example_json!")
	//fmt.Println("jsonfile: ", jsonfile)

	json := parse_json_file(jsonfile)
	//json := parse_json_file("app1.json")
	//fmt.Println("\t", "json", reflect.TypeOf(json))
	fmt.Println(json["name"], json["statusCode"])

}

func parse_health_checker_json(jsonString string, depth string) {

	var jsonMap map[string]interface{}
	json.Unmarshal([]byte(jsonString), &jsonMap)

	if depth == "dynamic" {
		comp := jsonMap["components"]
		broken_components := make([]map[string]interface{}, 0)

		for _, value := range comp.([]interface{}) {
			value_map := value.(map[string]interface{})
			if value_map["statusCode"] != "OK" {
				broken_components = append(broken_components, value_map)
			}
		}
		jsonMap["broken_components"] = broken_components
		delete(jsonMap, "components")
		dynamic_json, err := json.MarshalIndent(jsonMap, "", "\t")
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(string(dynamic_json))
	} else if depth == "short" {
		short_output := ShortOutput{Name: jsonMap["name"].(string), StatusCode: jsonMap["statusCode"].(string)}
		short_json, err := json.MarshalIndent(short_output, "", "\t")
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(string(short_json))
	} else if depth == "full" {
		full_json, err := json.MarshalIndent(jsonMap, "", "\t")
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(string(full_json))
	}
}

func parseArgs() (*Options, error) {
	options := &Options{}

	flag.StringVar(&options.HostHeader, "hostHeader", "", "override Host specified in URL")
	flag.StringVar(&options.JsonFile, "jsonFile", "", "relative path to health_checker json file")
	flag.StringVar(&options.Url, "url", "", "url to check")
	flag.StringVar(&options.Depth, "depth", "dynamic", "Determine amount/type of data to return")
	flag.Usage = func() {
		fmt.Printf("Usage: health_checker-go [options]\n\n")
		flag.PrintDefaults()
	}
	flag.Parse()

	return options, nil
}

func main() {
	options, err := parseArgs()
	if err != nil {
		os.Exit(1)
	}

	//Depth flag error checking
	if options.Depth != "dynamic" && options.Depth != "short" && options.Depth != "full" {
		fmt.Println("Error: Depth flag not understood. Must be one of the following: ['dynamic', 'short', 'full']")
		return
	}

	if len(options.Url) > 0 {
		response := health_checker_http_req(options.Url, options.HostHeader)
		parse_health_checker_json(response, options.Depth)
	}

	if len(options.JsonFile) > 0 {
		example_json(options.JsonFile)
	}
}