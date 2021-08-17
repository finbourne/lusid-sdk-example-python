<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

# Python SDK Example

## Installation

Install the LUSID SDK and dependencies via the `requirements.txt`

```
$ pip install -r requirements.txt
```

or if you are running as a non privileged user you may prefer to install specifically for your user account:

```
$ pip install --user -r requirements.txt
```

## Running

The example `main.py` script requires either a [Personal Access Token (PAT)](https://support.lusid.com/knowledgebase/article/KA-01774/en-us) or [API credentials](https://support.lusid.com/knowledgebase/article/KA-01663/) to be configured first.

### PAT

To run the script using a PAT pass in the token and LUSID API url e.g.

```
$ python main.py -k <your secret PAT> -u https://demo.lusid.com/api
```

### API Credentials

API credentials can be configured as environment variables or supplied via a file, see [here](https://support.lusid.com/knowledgebase/article/KA-01663/) for details on how to do this.

To run the script using credentials configured as environment variables, run the following:

```
$ python main.py 
```

To run the script passing credentials via a file, run the following:

```
$ python main.py -c <path to credentials file>
```

For more help running the script run

```
$ python main.py -h
```